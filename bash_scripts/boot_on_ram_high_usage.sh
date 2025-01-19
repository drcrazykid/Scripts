#!/bin/bash

# Get total and used memory in percentage
mem_usage=$(free | awk '/^Mem:/ {print $3/$2 * 100.0}')

# Convert to an integer for comparison
mem_usage=${mem_usage%.*}

# File to track how long RAM has been over 95%
log_file="/tmp/high_ram_count.log"

# Threshold for memory usage and duration
threshold=95
max_duration=5 # In minutes

if (( mem_usage >= threshold )); then
    # Increment the count or start tracking
    if [[ -f "$log_file" ]]; then
        count=$(cat "$log_file")
        ((count++))
    else
        count=1
    fi
    echo $count > "$log_file"

    # If RAM usage persists for 5 minutes, reboot
    if (( count >= max_duration )); then
        echo "$(date): RAM usage exceeded $threshold% for $max_duration minutes. Rebooting." >> /var/log/high_ram_reboots.log
        rm -f "$log_file"
        /sbin/reboot
    fi
else
    # Reset the count if memory usage is below the threshold
    rm -f "$log_file"
fi