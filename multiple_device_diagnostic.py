for i in range(5):
    equipment_name = input("Entrez le nom de l'équipement : ")
    cpu_usage = float(input("Entrez la consommation en CPU (%) de l'équipement :"))

    print("DEVICE ", equipment_name)
    print("CPU ", cpu_usage, "%")
    if cpu_usage >= 90:
        print("STATUS : CRITICAL")
    elif cpu_usage >= 70:
        print("STATUS : WARNING")
    else:
        print("STATUS : NORMAL")
     