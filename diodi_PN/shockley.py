import numpy as np
import matplotlib.pyplot as plt

# Parametri tipici per un diodo di segnale come il 1N4148
Is = 2.68e-9  # Corrente di saturazione inversa (Ampere)
n = 1.83      # Fattore di idealità 
Vt = 0.02585  # Tensione termica a 300K (Volt)

# Generiamo un array di tensioni (da -1V a 0.8V per vedere anche la zona inversa)
Vd = np.linspace(-1.0, 0.8, 500)

# Equazione di Shockley
Id = Is * (np.exp(Vd / (n * Vt)) - 1)

# Creazione del grafico
plt.figure(figsize=(10, 6))
plt.plot(Vd, Id, label='1N4148 Characteristic', color='red', linewidth=2)

# Formattazione del grafico
plt.title('Curva Caratteristica I-V del Diodo 1N4148')
plt.xlabel('Tensione ai capi del diodo (V)')
plt.ylabel('Corrente (A)')
plt.grid(True, which='both', linestyle='--', alpha=0.5)
plt.axhline(0, color='black', linewidth=1) # Asse X
plt.axvline(0, color='black', linewidth=1) # Asse Y

# Limitiamo l'asse Y per vedere bene la curva senza che "esploda" verso l'alto
plt.ylim(-0.01, 0.1) 

plt.legend()
plt.show()
