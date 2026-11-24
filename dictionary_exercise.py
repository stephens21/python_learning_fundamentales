device = {
    "name": "Router-01",
    "ip": "192.168.1.1",
    "type": "Router",
    "brand": "Cisco",
    "cpu": 45.5,
    "online": True
}

print(device['name'])
print(device['ip'])
print(device['type'])
print(device['brand'])
device['cpu'] = 78.5
device['temperature'] = 65.8
device['memory'] = 72.0
for key in device:
    if 'ip' in device:
        print("IP ADDRESS FOUND")
    else:
        print("IP ADDRESS NOT FOUND")

for key, value in device.items():
    print(key, ":", value)