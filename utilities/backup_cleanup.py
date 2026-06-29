import os
import time

# Directory containing backups (update as needed)
BACKUP_DIR = "/var/backups"

# Retention period (in days)
RETENTION_DAYS = 30

def cleanup_backups():
    now = time.time()
    cutoff = now - (RETENTION_DAYS * 24 * 60 * 60)
    removed_files = []

    if not os.path.exists(BACKUP_DIR):
        print(f"❌ Backup directory '{BACKUP_DIR}' not found.")
        return

    for root, dirs, files in os.walk(BACKUP_DIR):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                if os.path.getmtime(file_path) < cutoff:
                    os.remove(file_path)
                    removed_files.append(file_path)
            except Exception as e:
                print(f"❌ Error removing {file_path}: {e}")

    if removed_files:
        print("✅ Cleanup complete. Removed old backups:")
        for f in removed_files:
            print(" -", f)
    else:
        print("No old backups found.")

if __name__ == "__main__":
    cleanup_backups()
