equipment_name = input("Entrez le nom de l'équipement : ")
equipment_ip = input("Entrez l'adresse IP de l'équipement : ")
equipment_cpu = float(input("Entrez l'utilisation en cpu (%) : "))
equipment_memory = float(input("Entrez l'utilisation en mémoire RAM (%): "))
temperature = float(input("Entrez la température de l'équipement (°C): "))
online_status = input("Entrez le statut de l'équipement (True/False) : ").lower() == "true"


print("================================================")
print("\tDEVICE DIAGNOSTIC REPORT")
print("================================================")
print("Equipment Name: " + equipment_name)
print("Equipment IP: " + equipment_ip)
if equipment_cpu >= 90 :
    print("Equipment CPU: " + str(equipment_cpu), "%", " - ", "CRITICAL")
elif equipment_cpu >= 70:
    print("Equipment CPU: " + str(equipment_cpu), "%", " - ", "WARNING")
else:
    print("Equipment CPU: " + str(equipment_cpu), "%", " - ", "NORMAL")

if equipment_memory >= 90 :
    print("Equipment RAM: " + str(equipment_memory), "%", " - ", "CRITICAL")
elif equipment_memory >= 75:
    print("Equipment RAM: " + str(equipment_memory), "%", " - ", "WARNING")
else:
    print("Equipment RAM: " + str(equipment_memory), "%", " - ", "NORMAL")

if temperature >= 80 :
    print("Temperature: " + str(temperature), "°C", " - ", "CRITICAL")
elif temperature >= 70:
    print("Temperature: " + str(temperature), "°C", " - ", "WARNING")
else:
    print("Temperature: " + str(temperature), "°C", " - ", "NORMAL")

if online_status == True:
    print("DEVICE ONLINE")
else:
     print("DEVICE OFFLINE")


print("================================================")