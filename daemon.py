import daemon
import os
import signal
import subprocess
import time

def start_child_process():
    subprocess.Popen(["python", "-m", "assetpulse.filesystem.crawl"])
    # subprocess.Popen(["python", "-m", "assetpulse.filesystem", "--top", "/", "--regex-patterns", "your_regex_patterns_here"])

def sigterm_handler(signum, frame):
    print("Received SIGTERM. Exiting...")
    os._exit(0)

def start_daemon():
    signal.signal(signal.SIGTERM, sigterm_handler)
    while True:
        start_child_process()
        time.sleep(60)  # Adjust as needed