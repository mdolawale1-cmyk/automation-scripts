import os
import time

# Directory to clean (change as needed)
TARGET_DIR = "/tmp"

# File extensions to remove
EXTENSIONS = [".log", ".tmp", ".bak"]

# Age threshold (in seconds) — here: 7 days
AGE_THRESHOLD = 7 * 24 * 60 * 60

def cleanup_files():
    now = time.time()
    removed_files = []

    for root, dirs, files in os.walk(TARGET_DIR):
        for file in files:
            if any(file.endswith(ext) for ext in EXTENSIONS):
                file_path = os.path.join(root, file)
                file_age = now - os.path.getmtime(file_path)

                if file_age > AGE_THRESHOLD:
                    try:
                        os.remove(file_path)
                        removed_files.append(file_path)
                    except Exception as e:
                        print(f"❌ Error removing {file_path}: {e}")

    if removed_files:
        print("✅ Cleanup complete. Removed files:")
        for f in removed_files:
            print(" -", f)
    else:
        print("No old temp files found.")

if __name__ == "__main__":
    cleanup_files()
