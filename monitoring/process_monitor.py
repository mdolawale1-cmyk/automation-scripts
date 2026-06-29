import psutil
import datetime

# List of critical processes to monitor
CRITICAL_PROCESSES = ["nginx", "mysqld", "sshd"]

# Output log file
LOG_FILE = "process_monitor.log"

def check_processes():
    running_processes = [p.name() for p in psutil.process_iter()]
    report_lines = []

    for proc in CRITICAL_PROCESSES:
        if proc in running_processes:
            report_lines.append(f"{proc}: ✅ Running")
        else:
            report_lines.append(f"{proc}: ❌ Not running")

    return report_lines

def log_report(report_lines):
    with open(LOG_FILE, "a") as log:
        log.write(f"\n=== Process Monitor Report ({datetime.datetime.now()}) ===\n")
        for line in report_lines:
            log.write(line + "\n")

if __name__ == "__main__":
    report = check_processes()
    for line in report:
        print(line)
    log_report(report)
    print(f"📄 Report saved to {LOG_FILE}")
