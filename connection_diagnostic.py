equipment_name = input("Entrez le nom de l'équipement : ")
equipment_ip = input("Entrez l'adresse IP de l'équipement : ")

online_status = input("Entrez le statut de l'équipement (True/False) : ").lower() == "true"

if not online_status:
    print( equipment_name, " OFFILNE")
elif online_status and equipment_ip != "":
    print(equipment_name, " CONNECTED")
else:
    print("CONNECTION ISSUE")