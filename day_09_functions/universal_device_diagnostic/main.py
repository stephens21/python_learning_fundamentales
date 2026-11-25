from cpu_diagnostic import diagnostic_cpu_function
from memory_diagnostic import diagnostic_memory
from temperature_diagnostic import diagnostic_temperature_function


device_name = "Router-01"

cpu = 95
memory = 80
temperature = 72

cpu_status = diagnostic_cpu_function(cpu)
memory_status = diagnostic_memory(memory)
temperature_status = diagnostic_temperature_function(temperature)

print("DEVICE DIAGNOSTIC REPORT")
print("------------------------")
print("Device:", device_name)
print("CPU:", cpu_status)
print("MEMORY:", memory_status)
print("TEMPERATURE:", temperature_status)