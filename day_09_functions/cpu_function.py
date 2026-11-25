def diagnostic_cpu(cpu_usage):
    if cpu_usage >= 90:
        return "CRITICAL"
    elif cpu_usage >= 70:
        return "WARNING"
    else:
        return "NORMAL"

cpu_95 = diagnostic_cpu(95)
print(cpu_95)

cpu_75 = diagnostic_cpu(75)
print(cpu_75)

cpu_45 = diagnostic_cpu(45)
print(cpu_45)        