# controller.py
import socket

# CHANGE THIS to your Ubuntu machine's IP address
TARGET_IP = '192.168.X.X'
PORT = 5555

def connect_to_agent():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((TARGET_IP, PORT))
        print("[+] Connected to agent!\n")

        while True:
            # Wait for prompt from agent
            response = client.recv(4096).decode()
            print(response, end='')

            # Send command input to agent
            cmd = input()
            client.send(cmd.encode())

            if cmd.strip().lower() == "exit":
                print("[*] Closing connection.")
                break

            # Receive response
            response = client.recv(8192).decode()
            print(response)

    except Exception as e:
        print(f"[!] Connection error: {e}")
    finally:
        client.close()

if __name__ == "__main__":
    connect_to_agent()
