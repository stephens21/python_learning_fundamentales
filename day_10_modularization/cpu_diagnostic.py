
def diagnostic_cpu(cpu_usage):
    if cpu_usage >= 90:
        return "CRITICAL"
    elif cpu_usage >= 70:
        return "WARNING"
    else:
        return "NORMAL"