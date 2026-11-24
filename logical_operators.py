cpu_usage = 95
memory_usage = 85
temperature = 75
online_status = True

if cpu_usage >= 90 and memory_usage >= 90:
    print("CRITICAL: CPU AND RAM OVERLOAD")

if cpu_usage >= 90 or memory_usage >= 90:
    print("WARNING: RESOURCE  ALERT")
if temperature >= 80 or cpu_usage >= 90:
    print("WARNING: RESOURCE OR TEMPERATURE ALERT")

if not online_status:
    print("CRITICAL: DEVICE OFFLINE")

if online_status and cpu_usage >= 90:
    print("CRITICAL")