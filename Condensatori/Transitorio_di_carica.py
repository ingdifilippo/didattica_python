import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate # Se non l'hai, usa: pip install tabulate

# --- Parametri del Circuito ---
E = 12       # Tensione del generatore [V]
R = 1000    # Resistenza [Ohm] (10k)
C = 1e-6     # Capacità [Farad] (1uF)
tau = R * C  # Costante di tempo

# --- Generazione Dati ---
t = np.linspace(0, 5 * tau, 500)
v_c = E * (1 - np.exp(-t / tau))        # Tensione
i_c = (E / R) * np.exp(-t / tau)         # Corrente

# --- Calcolo multipli di Tau ---
multipli_tau = np.array([1, 2, 3, 4, 5])
tempi_tau = multipli_tau * tau
v_tau = E * (1 - np.exp(-tempi_tau / tau))
i_tau = (E / R) * np.exp(-tempi_tau / tau)

# --- Tabella di Output ---
dati_tabella = []
for m in multipli_tau:
    perc_v = (1 - np.exp(-m)) * 100
    perc_i = (np.exp(-m)) * 100
    dati_tabella.append([f"{m}τ", f"{perc_v:.2f}%", f"{(perc_v/100)*E:.2f}", f"{perc_i:.2f}%", f"{(perc_i/100)*(E/R):.4f}"])

print("\nPercentuali di Carica rispetto ai multipli di Tau:")
print(tabulate(dati_tabella, headers=["Tempo", "% Tensione (V_c/E)", "Tensione [Volt]", "% Corrente (i/Imax)",  "Corrente [Ampere]"], tablefmt="grid"))


# --- Grafico ---
fig, ax1 = plt.subplots(figsize=(10, 6))

# Asse Tensione (Sinistra)
ax1.set_xlabel('Tempo (s)')
ax1.set_ylabel('Tensione V_c (V)', color='tab:blue')
ax1.plot(t, v_c, color='tab:blue', label='Tensione V_c', linewidth=2)
ax1.tick_params(axis='y', labelcolor='tab:blue')
ax1.grid(True, linestyle='--', alpha=0.6)

# Asse Corrente (Destra)
ax2 = ax1.twinx()
ax2.set_ylabel('Corrente i (A)', color='tab:red')
ax2.plot(t, i_c, color='tab:red', linestyle='--', label='Corrente i', linewidth=2)
ax2.tick_params(axis='y', labelcolor='tab:red')

# Evidenziazione multipli di Tau
for mt, vt, it in zip(multipli_tau, v_tau, i_tau):
    ax1.plot(mt * tau, vt, 'ko') # Punto sulla curva tensione
    ax1.annotate(f'{vt:.2f}', (mt * tau, vt), textcoords="offset points", xytext=(0,10), ha='center')

# Evidenziazione multipli di Tau
for mt, vt, it in zip(multipli_tau, v_tau, i_tau):
    ax2.plot(mt * tau, it, 'ko') # Punto sulla curva tensione
    ax2.annotate(f'{it:.2e}', (mt * tau, it), textcoords="offset points", xytext=(0,10), ha='center')

plt.title('Transitorio di Carica del Condensatore (RC)')
fig.tight_layout()
plt.show()
