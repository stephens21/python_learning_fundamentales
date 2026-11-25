def diagnostic_cpu(cpu_usage):
    if cpu_usage >= 90:
        return "CRITICAL"
    elif cpu_usage >= 70:
        return "WARNING"
    else:
        return "NORMAL"

def diagnostic_memory(memory_usage):
    if memory_usage >= 90:
        return "CRITICAL"
    elif memory_usage >= 75:
        return "WARNING"
    else:
        return "NORMAL"


def diagnostic_temperature(temperature):
    if temperature >= 80:
        return "CRITICAL"
    elif temperature >= 65:
        return "WARNING"
    else:
        return "NORMAL"


equipment_name = input("Entrez le nom de l'équipement : ")
cpu_usage = float(input("Entrez le consommation en CPU(%) : "))
memory_usage = float(input("Entrez la consommation en mémoire RAM(%) : "))
temperature = float(input("Entrez la consommation en temperature(°C) du device : "))

print("DEVICE DIAGNOSTIC REPORT")
print("----------------------------")
print(f'Device: {equipment_name}')
print(f'CPU: {diagnostic_cpu(cpu_usage)}')
print(f'MEMORY: {diagnostic_memory(memory_usage)}')
print(f'TEMPERATURE: {diagnostic_temperature(temperature)}')