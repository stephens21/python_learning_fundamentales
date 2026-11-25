from cpu_diagnostic import diagnostic_cpu_function
from memory_diagnostic import diagnostic_memory
from temperature_diagnostic import diagnostic_temperature_function

def analyze_device(cpu, memory, temperature):
    cpu_status = diagnostic_cpu_function(cpu)
    memory_status = diagnostic_memory(memory)
    temperature_status = diagnostic_temperature_function(temperature)

    return cpu_status, memory_status, temperature_status

cpu_result, memory_result, temperature_result = analyze_device(95,80,72)
print(f'CPU : {cpu_result}')
print(f'RAM : {memory_result}')
print(f'TEMPERATURE : {temperature_result}')


