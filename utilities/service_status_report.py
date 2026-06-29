import subprocess
import datetime

# List of critical services to monitor
SERVICES = ["nginx", "mysql", "ssh"]

# Output report file
REPORT_FILE = "service_status_report.txt"

def check_service_status(service):
    try:
        result = subprocess.run(
            ["systemctl", "is-active", service],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        status = result.stdout.strip()
        return status
    except Exception as e:
        return f"Error: {e}"

def generate_report():
    with open(REPORT_FILE, "w") as report:
        report.write("=== Daily Service Status Report ===\n")
        report.write(f"Generated on: {datetime.datetime.now()}\n\n")
        for service in SERVICES:
            status = check_service_status(service)
            report.write(f"{service}: {status}\n")
    print(f"✅ Report generated: {REPORT_FILE}")

if __name__ == "__main__":
    generate_report()
