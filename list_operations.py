devices = ["Router-01", "Switch-01", "Server-01"]

devices.append("Firewall-01")
devices.append("Printer-01")
devices[1] = "Core-Switch-01"
devices.remove("Printer-01")
print(devices)
print(len(devices))