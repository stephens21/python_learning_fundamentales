def diagnostic_temperature_function(temperature):
    if temperature >= 80:
        return "CRITICAL"
    elif temperature >= 65:
        return "WARNING"
    else:
        return "NORMAL"