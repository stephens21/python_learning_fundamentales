cpu_usage = input("Entrez la consommation en CPU (%): ")
memory_usage = input("Entrez la consommation en memoire RAM (%): ")

if cpu_usage >= 90 and memory_usage >= 90:
    print("CRITICAL")
elif cpu_usage >= 90 or memory_usage >= 90:
    print("WARNING")
else:
    print("NORMAL")