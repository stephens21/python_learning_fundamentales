devices = [
    "Router-01",
    "Switch-01",
    "Server-01",
    "Firewall-01",
    "Camera-01"
]

for device in devices:
    print(device)

for device in devices:
    print("checking device...", device)

print(len(devices))

for device in devices:
    if "Server-01" == device:
        print("Server-01 FOUND")
    else:
        print("Server-01 NOT FOUND")

for device in devices:
    if "Printer-01" == device:
        print("Printer-01 FOUND")
    else:
        print("Printer-01 NOT FOUND")
