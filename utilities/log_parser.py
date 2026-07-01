"""Parses system logs and summarizes errors/warnings for reporting."""

import sys

def parse_log(file_path):
    error_count = 0
    warning_count = 0

    try:
        with open(file_path, "r") as log_file:
            for line in log_file:
                if "ERROR" in line:
                    error_count += 1
                elif "WARNING" in line:
                    warning_count += 1

        print("=== Log Summary ===")
        print(f"Errors: {error_count}")
        print(f"Warnings: {warning_count}")

    except FileNotFoundError:
        print(f"❌ Log file '{file_path}' not found.")
    except Exception as e:
        print(f"❌ Error parsing log file: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python log_parser.py <log_file>")
    else:
        parse_log(sys.argv[1])
