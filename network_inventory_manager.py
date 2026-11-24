devices = []

print("Veuillez enregistrer le nom de 5 équipements")

count = 1


for count in range(1, 6):
    equipment = input("Enter device ", count, ":")
    devices.append(equipment)

print("================================")
print("NETWORK DEVICE INVENTORY")
print("================================")

print("Total devices registered :", len(devices))

print("Registered devices :")
print(devices)

search = input("Enter the device you are looking for :")
print("Searched device : ", search)
for device in devices:
    if search == device:
        print("DEVICE FOUND")
    else:
        print("DEVICE NOT FOUND")