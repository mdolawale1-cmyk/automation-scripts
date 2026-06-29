import shutil
import datetime

# Threshold for disk usage (in %)
THRESHOLD = 80

# Directory to check (root by default)
CHECK_DIR = "/"

def check_disk_usage(path):
    usage = shutil.disk_usage(path)
    percent_used = (usage.used / usage.total) * 100
    return percent_used

def alert_if_exceeded():
    percent_used = check_disk_usage(CHECK_DIR)
    print(f"Current disk usage: {percent_used:.2f}%")

    if percent_used > THRESHOLD:
        print(f"🚨 ALERT: Disk usage exceeded {THRESHOLD}%!")
        # Example action: log to file
        with open("disk_alert.log", "a") as log:
            log.write(f"{datetime.datetime.now()}: High disk usage detected - {percent_used:.2f}%\n")
        # You could also integrate with alert_email.py here
    else:
        print("✅ Disk usage is within safe limits.")

if __name__ == "__main__":
    alert_if_exceeded()
