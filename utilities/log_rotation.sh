#!/bin/bash

# Directory containing logs
LOG_DIR="/var/log/myapp"

# Number of days to keep old logs
RETENTION_DAYS=7

# Timestamp for rotated files
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")

# Ensure log directory exists
if [ ! -d "$LOG_DIR" ]; then
    echo "❌ Log directory $LOG_DIR not found."
    exit 1
fi

# Rotate and compress logs
for logfile in "$LOG_DIR"/*.log; do
    if [ -f "$logfile" ]; then
        rotated_file="${logfile}_${TIMESTAMP}.gz"
        gzip -c "$logfile" > "$rotated_file"
        echo "🔄 Rotated and compressed: $logfile → $rotated_file"
        # Clear original log
        : > "$logfile"
    fi
done

# Cleanup old rotated logs
find "$LOG_DIR" -name "*.gz" -type f -mtime +$RETENTION_DAYS -exec rm -f {} \;
echo "✅ Cleanup complete. Old logs older than $RETENTION_DAYS days removed."
