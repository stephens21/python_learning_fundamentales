equipment_name = input("Entrez le nom de l'équipement : ")
equipment_ip = input("Entrez l'adresse IP de l'équipement : ")
equipment_cpu = float(input("Entrez l'utilisation en cpu (%) : "))
equipment_memory = float(input("Entrez l'utilisation en mémoire RAM (%): "))
temperature = float(input("Entrez la température de l'équipement (°C): "))
online_status = input("Entrez le statut de l'équipement (True/False) : ").lower() == "true"

if not online_status:
    print("CRITICAL : ", equipment_name, " OFFLINE")
elif equipment_cpu >= 90 and equipment_memory >= 90:
    print("CRITICAL : CPU AND RAM OVERLOAD")
elif equipment_cpu >= 90 or equipment_memory >= 90:
    print("WARNING : RESOURCE OVERLOAD")
elif temperature >= 80:
    print("CRITICAL : HIGH TEMPERATURE")
elif temperature >= 70:
    print("WARNING : HIGH TEMPERATURE")
else:
    print("SYSTEM NORMAL")