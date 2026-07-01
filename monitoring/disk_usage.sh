# Monitors disk usage and logs alert if usage exceeds threshold
#!/bin/bash

# Threshold for disk usage (in %)
THRESHOLD=80

# Check disk usage for root partition
USAGE=$(df -h / | awk 'NR==2 {print $5}' | sed 's/%//')

echo "Current disk usage: $USAGE%"

if [ "$USAGE" -gt "$THRESHOLD" ]; then
    echo "🚨 ALERT: Disk usage is above $THRESHOLD%!"
    # Example action: log to file
    echo "$(date): High disk usage detected - $USAGE%" >> disk_alert.log
    # You could also send an email or trigger monitoring here
else
    echo "✅ Disk usage is within safe limits."
fi
