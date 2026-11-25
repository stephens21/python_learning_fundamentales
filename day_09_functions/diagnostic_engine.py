devices = []

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


print("================================")
print("DEVICE INVENTORY")
print("================================")

for i in range(1, 4):
    device = {}
    print(f'Enter the following data for the device {i}:')
    device['name'] = input("Enter the name : ")
    device['cpu'] = float(input('Enter the CPU (%) consomption : '))
    device['memory'] = float(input('Enter the RAM (°C) consomption : '))
    device['temperature'] = float(input('Enter the temperature : '))
    devices.append(device)

print(f'\nTotal devices registered : {len(devices)}')

for item in devices:
    print("\n=======================================================")
    print(f"Diagnostic Analyze Result from Device {item['name']}")
    print("=======================================================")
    cpu_usage = diagnostic_cpu(item['cpu'])
    memory_usage = diagnostic_memory(item['memory'])
    temperature = diagnostic_temperature(item['temperature'])
    print(f'CPU Device is {cpu_usage}')
    print(f'RAM Device is {memory_usage}')
    print(f'TEMPERATURE Device is {temperature}')

