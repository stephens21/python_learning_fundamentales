equipment_name = input("Entrez le nom de l'équipement : ")
equipment_ip = input("Entrez l'adresse IP de l'équipement : ")
checking_number = 1

while checking_number <=5:
    cpu_usage = float(input("Entrez la consommation en CPU (%) de l'équipement :"))

    print("==========================")
    print("NETWORK MONITORING")
    print("Equipment:", equipment_name)
    print("IP:", equipment_ip)
    print("Check:", checking_number)
    if cpu_usage >= 90:
        print("STATUS : CRITICAL")
    elif cpu_usage >= 70:
        print("STATUS : WARNING")
    else:
        print("STATUS : NORMAL")

    checking_number += 1


