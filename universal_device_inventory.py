devices = []


print("================================")
print("UNIVERSAL DEVICE INVENTORY")
print("================================")

for i in range(1, 4):
    device = {}
    print(f'Enter the following data for the device {i}:')
    device['name'] = input("Enter the name : ")
    device['ip'] = input ('Enter the IP address : ')
    device['type']= input('Enter the category : ')
    device['brand'] = input('Enter the brand : ')
    device['cpu'] = float(input('Enter the CPU (%) consomption : '))
    device['memory'] = float(input('Enter the RAM (°C) consomption : '))
    device['temperation'] = float(input('Enter the temperature : '))
    device['status'] = input('Enter the status (False/True) : ').lower() == "true"
    devices.append(device)

print(f'Total devices registered : {len(devices)}')

for key, value in devices.item():
    print(key, " : ", value)

for item in devices:
    if item['cpu'] >= 90:
        print(f'Device {item['name']} is in CRITICAL STATUS')
    elif item['cpu'] >= 70:
        print(f'Device {item['name']} is in WARNING STATUS')
    else:
        print(f'Device {item['name']} is in NORMAL STATUS')