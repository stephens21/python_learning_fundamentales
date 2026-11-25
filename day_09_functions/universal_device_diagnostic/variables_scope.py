total_devices = 0
platform_name = "UNIVERSAL DEVICE DIAGNOSTIC"

def register_device():
    global total_devices
    total_devices +=1
    return total_devices

def display_platform():
    return platform_name

while total_devices <5:
    register_device()

print(f'Total devices : {total_devices}')
print(f'{display_platform()}')