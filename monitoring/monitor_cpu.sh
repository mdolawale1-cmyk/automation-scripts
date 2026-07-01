"""Tracks CPU usage and generates alert when usage is high."""
#!/bin/bash

# Threshold for CPU usage (in %)
THRESHOLD=80

# Get current CPU usage (average over 1 minute)
CPU_USAGE=$(top -bn1 | grep "Cpu(s)" | \
            awk '{print $2 + $4}')

# Round CPU usage to integer
CPU_INT=$(printf "%.0f" "$CPU_USAGE")

echo "Current CPU usage: $CPU_INT%"

if [ "$CPU_INT" -gt "$THRESHOLD" ]; then
    echo "🚨 ALERT: CPU usage is above $THRESHOLD%!"
    # Example action: log to file
    echo "$(date): High CPU usage detected - $CPU_INT%" >> cpu_alert.log
    # You could also send an email or trigger monitoring here
else
    echo "✅ CPU usage is within safe limits."
fi
