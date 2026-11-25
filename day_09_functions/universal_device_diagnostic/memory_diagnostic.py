def diagnostic_memory(memory_usage):
    if memory_usage >= 90:
        return "CRITICAL"
    elif memory_usage >= 75:
        return "WARNING"
    else:
        return "NORMAL"