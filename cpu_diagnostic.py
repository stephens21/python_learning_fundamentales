cpu_usage = input("Entrez l'utilisation du CPU (en %) : ")

if cpu_usage > 90:
    print("CRITICAL CPU ALERT")
elif cpu_usage >= 70 & cpu_usage < 90:
    print("WARNING CPU ALERT")
else:
    print("NORMAL CPU ALERT")


    