def diagnostic_cpu(cpu_usage=50):
    if cpu_usage >= 90:
        return "CRITICAL"
    elif cpu_usage >= 70:
        return "WARNING"
    else:
        return "NORMAL"

cpu_95 = diagnostic_cpu(95)
cpu_75 = diagnostic_cpu(75)
cpu_40 = diagnostic_cpu(40)
print(cpu_95)
print(f'\n{cpu_75}')
print(f'\n{cpu_40}')