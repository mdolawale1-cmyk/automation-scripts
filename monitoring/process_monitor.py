"""Monitors critical system processes and logs their status."""

import psutil
import datetime

# List of critical processes to monitor
CRITICAL_PROCESSES = ["nginx", "mysqld", "sshd"]

def check_processes():
    running = [p.info["name"] for p in psutil.process_iter(attrs=["name"])]
    status_report = {}
    for proc in CRITICAL_PROCESSES:
        status_report[proc] = "Running ✅" if proc in running else "Not Running ❌"
    return status_report

def log_status(report):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("process_monitor.log", "a") as log_file:
        log_file.write(f"\n[{timestamp}] Process Status:\n")
        for proc, status in report.items():
            log_file.write(f" - {proc}: {status}\n")

if __name__ == "__main__":
    report = check_processes()
    log_status(report)
    print("Process monitoring complete. Status logged.")
