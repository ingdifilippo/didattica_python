import numpy as np
import matplotlib.pyplot as plt

# --- Costanti Fisiche ---
k = 1.380649e-23  # Costante di Boltzmann (J/K)
q = 1.60217663e-19 # Carica dell'elettrone (C)

# --- Parametri del Diodo (1N4148 a 25°C) ---
Is_ref = 2.68e-9  # Is di riferimento (Ampere)
T_ref_C = 25.0    # Temperatura di riferimento (Celsius)
n = 1.83          # Fattore di idealità

# Convertiamo T_ref in Kelvin
T_ref_K = T_ref_C + 273.15

# --- Definizione delle tre temperature da testare (in Celsius) ---
temperature_C = [0, 25, 75]
colori = ['blue', 'green', 'red'] # Colori per differenziare le curve

# Generiamo un array di tensioni (focus sulla zona di conduzione)
Vd = np.linspace(0.0, 0.9, 500)

plt.figure(figsize=(12, 7))

# --- Ciclo per calcolare e tracciare le curve per ogni temperatura ---
for T_C, colore in zip(temperature_C, colori):
    # 1. Convertiamo in Kelvin
    T_K = T_C + 273.15
    
    # 2. Ricalcoliamo la Tensione Termica Vt(T)
    Vt = (k * T_K) / q
    
    # 3. Ricalcoliamo la Corrente di Saturazione Is(T)
    # Questa formula approssima l'aumento esponenziale di Is con T
    # (raddoppia ogni ~10°C, basato sulla gap energetica del silicio)
    Is_T = Is_ref * np.exp( (T_K - T_ref_K) * 0.07 ) # 0.07 è un coefficiente tipico per il Si

    # 4. Applichiamo l'equazione di Shockley
    Id = Is_T * (np.exp(Vd / (n * Vt)) - 1)
    
    # 5. Tracciamo la curva
    etichetta = f'T = {T_C}°C'
    plt.plot(Vd, Id, label=etichetta, color=colore, linewidth=2.5)

# --- Formattazione Avanzata del Grafico ---
plt.title('Effetto della Temperatura sulla Curva I-V del Diodo 1N4148')
plt.xlabel('Tensione ai capi del diodo $V_D$ (V)')
plt.ylabel('Corrente nel diodo $I_D$ (A)')

# Miglioriamo la griglia
plt.grid(True, which='both', linestyle='--', alpha=0.7)
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)

# Limitiamo gli assi per vedere bene il "ginocchio"
plt.ylim(-0.001, 0.06) # Fino a 60mA
plt.xlim(0.3, 0.9)     # Focus sulla zona di accensione

# Aggiungiamo la LEGENDA (posizione automatica migliore)
plt.legend(title="Legenda Temperature", loc='best', fontsize='large')

plt.show()
