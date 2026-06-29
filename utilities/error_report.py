import os

# Path to the log file (update as needed)
LOG_FILE = "application.log"

# Path to save the error report
REPORT_FILE = "error_report.txt"

def generate_error_report():
    if not os.path.exists(LOG_FILE):
        print(f"❌ Log file '{LOG_FILE}' not found.")
        return

    errors = []
    with open(LOG_FILE, "r") as f:
        for line in f:
            if "ERROR" in line or "Exception" in line:
                errors.append(line.strip())

    with open(REPORT_FILE, "w") as report:
        report.write("=== Error Report ===\n")
        report.write(f"Source log: {LOG_FILE}\n")
        report.write(f"Total errors found: {len(errors)}\n\n")
        for err in errors:
            report.write(err + "\n")

    print(f"✅ Error report generated: {REPORT_FILE}")
    if errors:
        print("Sample errors:")
        for e in errors[:5]:  # show first 5 errors
            print(" -", e)

if __name__ == "__main__":
    generate_error_report()
