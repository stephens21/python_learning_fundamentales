temperature = input("Entrez la température de l'équipement (en°C) :")

if temperature >= 80:
    print("CRITICAL")
elif temperature >= 70:
    print("WARNING")
elif temperature >= 50:
    print("MODERATE")
else:
    print("NORMAL")