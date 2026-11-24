devices = [
    {
        "name": "Router-01",
        "ip": "192.168.1.1",
        "type": "Router",
        "cpu": 45.5,
        "online": True
    },
    {
        "name": "Switch-01",
        "ip": "192.168.1.2",
        "type": "Switch",
        "cpu": 75.0,
        "online": True
    },
    {
        "name": "Server-01",
        "ip": "192.168.1.3",
        "type": "Server",
        "cpu": 95.0,
        "online": False
    }
]

print(len(devices))
print(devices)
for device in devices:
    print("===========================")
    print(f'Nom :{device['name']}')
    print(f'IP :{device["ip"]}')
    print(f'Type :{device["type"]}')
    print(f'CPU :{device['cpu']}')
    print(f'Online :{device["online"]}')
    