"""Monitors memory usage and triggers alert if threshold exceeded."""
#!/bin/bash

# Threshold for memory usage (in %)
THRESHOLD=80

# Get memory usage percentage
MEM_USAGE=$(free | awk '/Mem:/ {printf("%.0f", $3/$2 * 100)}')

echo "Current memory usage: $MEM_USAGE%"

if [ "$MEM_USAGE" -gt "$THRESHOLD" ]; then
    echo "🚨 ALERT: Memory usage is above $THRESHOLD%!"
    # Example action: log to file
    echo "$(date): High memory usage detected - $MEM_USAGE%" >> memory_alert.log
    # You could also send an email or trigger monitoring here
else
    echo "✅ Memory usage is within safe limits."
fi
