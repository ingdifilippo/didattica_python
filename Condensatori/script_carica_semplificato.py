import numpy as np
import matplotlib.pyplot as plt

# --- Parametri del Circuito ---

E = 12       # Tensione [V]
R = 1000     # Resistenza [Ohm]
C = 10e-6    # Capacità [F]

tau = R * C  # Costante di tempo
t_carica = 5 * tau  # Durata totale del transitorio


if tau < 0.1:
    print("Tau:", tau*1000, "ms")
    print("Tempo di carica: ", t_carica*1000, "ms")
else:
    print("Tau:", tau * 1000, "s")
    print("Tempo di carica: ", t_carica * 1000, "s")

print("\nValori significativi di tensione:\n ")

for i in range(0, 6):
    v_c = E*(1-np.exp(-i))
    print(i * tau, "s", v_c, "Volt")
    
    #print(f"{i * tau:.2f}", "s", f"{v_c:.2f}", "Volt") STAMPA ORDINATA  
    

