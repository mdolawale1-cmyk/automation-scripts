"""Consolidates system health checks (CPU, memory, disk, network, processes) into a single dashboard report."""

import psutil
import datetime
import socket

def check_cpu():
    return f"CPU Usage: {psutil.cpu_percent(interval=1)}%"

def check_memory():
    mem = psutil.virtual_memory()
    return f"Memory Usage: {mem.percent}%"

def check_disk():
    disk = psutil.disk_usage('/')
    return f"Disk Usage: {disk.percent}%"

def check_network():
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=2)
        return "Network: Connected ✅"
    except OSError:
        return "Network: Not Connected ❌"

def check_processes():
    critical = ["nginx", "mysqld", "sshd"]
    running = [p.info["name"] for p in psutil.process_iter(attrs=["name"])]
    results = []
    for proc in critical:
        status = "Running ✅" if proc in running else "Not Running ❌"
        results.append(f"{proc}: {status}")
    return "Processes: " + ", ".join(results)

def generate_report():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    report = [
        f"System Health Dashboard — {timestamp}",
        check_cpu(),
        check_memory(),
        check_disk(),
        check_network(),
        check_processes()
    ]
    return "\n".join(report)

if __name__ == "__main__":
    report = generate_report()
    with open("system_health_dashboard.log", "a") as f:
        f.write(report + "\n\n")
    print(report)
