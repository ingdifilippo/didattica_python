#Programma 1 - Calcolo della capacità del condensatore con dati utente
# Costante dielettrica del vuoto (F/m)
EPSILON_0 = 8.854e-12

print("--- Calcolatore Capacità Condensatore Piano ---")

# Input dell'utente

epsilon_r = float(input("Inserisci la costante dielettrica relativa (er): "))
area = float(input("Inserisci la superficie delle armature in m^2 (A): "))
distanza = float(input("Inserisci la distanza tra le armature in metri (d): "))

# Calcolo della capacità

capacita = (EPSILON_0 * epsilon_r * area) / distanza

# Stampa del risultato

print("\n--- Risultato ---")

print(f"La capacità del condensatore è: {capacita:.2e} Farad")

# conversione in picofarad per renderlo più leggibile
print(f"In picofarad (pF): {capacita * 1e12:.2f} pF")

