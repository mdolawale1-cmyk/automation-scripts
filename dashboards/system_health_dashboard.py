import psutil
import shutil
import datetime

# Thresholds
CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 80

REPORT_FILE = "system_health_dashboard.md"

def check_cpu():
    usage = psutil.cpu_percent(interval=1)
    return f"**CPU Usage:** {usage:.2f}% {'🚨 High' if usage > CPU_THRESHOLD else '✅ Normal'}"

def check_memory():
    mem = psutil.virtual_memory()
    return f"**Memory Usage:** {mem.percent:.2f}% {'🚨 High' if mem.percent > MEMORY_THRESHOLD else '✅ Normal'}"

def check_disk(path="/"):
    usage = shutil.disk_usage(path)
    percent_used = (usage.used / usage.total) * 100
    return f"**Disk Usage ({path}):** {percent_used:.2f}% {'🚨 High' if percent_used > DISK_THRESHOLD else '✅ Normal'}"

def check_processes(processes=["nginx", "mysqld", "sshd"]):
    running = [p.name() for p in psutil.process_iter()]
    results = []
    for proc in processes:
        if proc in running:
            results.append(f"{proc}: ✅ Running")
        else:
            results.append(f"{proc}: ❌ Not running")
    return "**Critical Processes:**\n" + "\n".join(results)

def generate_report():
    with open(REPORT_FILE, "w") as report:
        report.write("# 🖥️ System Health Dashboard\n")
        report.write(f"Generated on: {datetime.datetime.now()}\n\n")
        report.write(check_cpu() + "\n")
        report.write(check_memory() + "\n")
        report.write(check_disk("/") + "\n\n")
        report.write(check_processes() + "\n")
    print(f"📄 Dashboard generated: {REPORT_FILE}")

if __name__ == "__main__":
    generate_report()
