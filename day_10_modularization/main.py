from cpu_diagnostic import diagnostic_cpu
from memory_diagnostic import diagnostic_memory
from temperature_diagnostic import diagnostic_temperature


device = {}
print("================================")
print("DEVICE REGISTRATION")
print("================================")
device['name'] = input("Enter the name : ")
device['cpu'] = float(input('Enter the CPU (%) consomption : '))
device['memory'] = float(input('Enter the RAM (°C) consomption : '))
device['temperature'] = float(input('Enter the temperature : '))


cpu_usage = diagnostic_cpu(device['cpu'])
memory_usage = diagnostic_memory(device['memory'])
temperature = diagnostic_temperature(device['temperature'])

print("\n================================")
print("DEVICE DIAGNOSTIC REPORT")
print("================================")
print(f"Device:{device['name']}")
print(f"CPU:{cpu_usage}")
print(f"MEMORY:{memory_usage}")
print(f"TEMPERATURE:{temperature}")