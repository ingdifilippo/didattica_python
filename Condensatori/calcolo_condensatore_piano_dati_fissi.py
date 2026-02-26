#Programma 1 - Calcolo della capacità del condensatore con dati fissi

print("\nCalcolatore Capacità Condensatore Piano:")


# Costante dielettrica del vuoto (Farad/metro)

EPSILON_0 = 8.854e-12

# Costante dielettrica relativa (EPSILON_R) del materiale:

EPSILON_R = 5.5

# Area delle armature in metri quadri:

area = 0.04

# distanza tra le armature in millimetri:

distanza_mm = 3

distanza = distanza_mm / 1000


# Calcolo della capacità

capacita = (EPSILON_0 * EPSILON_R * area) / distanza

# Stampa del risultato in Farad:

print("\nC = ", capacita, "Farad")

# Stampa del risultato in nano Farad:

print("\nC = ", capacita * 10e9, "nano Farad (miliardesimi)")
