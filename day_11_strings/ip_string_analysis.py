device_ip = "192.168.1.100"

device_ip_split = device_ip.split('.')
print(device_ip_split[0])
print(device_ip_split[1])
print(device_ip_split[2])
print(device_ip_split[3])

print(f'Total device ip parts:{len(device_ip_split)}')

if device_ip.startswith("192"):
    print("Le device IP appartient à une plage privée")
else:
    print("Le device IP n'appartient pas à une plage privée")

