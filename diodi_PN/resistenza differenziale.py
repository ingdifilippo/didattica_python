import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

# Calcolo della tensione termica
q = 1.602E-19
T = 300
k_boltzman = 1.38E-23

V_termica = k_boltzman * T / q
I_sat = 1E-14

# Parametri del circuito
R = 220.0
V_cc = 5.0

V_start = 0
V_stop = 0.8
punti_di_calcolo = 1000

# Asse X
V_diodo = np.linspace(V_start, V_stop, punti_di_calcolo)

# Curva del diodo e retta di carico
I_diodo = I_sat * np.exp(V_diodo / V_termica)
I_carico = (V_cc - V_diodo) / R

# Calcolo del Punto di Lavoro (Q-Point)
def eq_intersezione(V):
    return I_sat * np.exp(V / V_termica) - (V_cc - V) / R

V_Q = fsolve(eq_intersezione, 0.7)[0]
I_Q = (V_cc - V_Q) / R

# --- NUOVO: Calcolo Resistenza Dinamica e Retta Tangente ---
# Conduttanza differenziale (g_d) e Resistenza dinamica (r_d)
g_d = I_Q / V_termica
r_d = 1 / g_d

print(f"Punto di Lavoro: V_Q = {V_Q:.4f} V, I_Q = {I_Q*1000:.2f} mA")
print(f"Resistenza dinamica nel Q-Point: r_d = {r_d:.2f} Ohm")

# Creo un intervallo di tensione stretto attorno a V_Q per disegnare la tangente
V_tangente = np.linspace(V_Q - 0.05, V_Q + 0.03, 100)
# Equazione della retta passante per (V_Q, I_Q) con pendenza g_d
I_tangente = g_d * (V_tangente - V_Q) + I_Q
# -----------------------------------------------------------

# Disegno il grafico
plt.figure(figsize=(10, 7))

plt.plot(V_diodo, I_diodo * 1000, color="orange", linewidth=2.5, label="Caratteristica Diodo")
plt.plot(V_diodo, I_carico * 1000, color="blue", linestyle="--", linewidth=1.5, label="Retta di Carico (Vcc=5V)")

# Traccio la retta tangente
plt.plot(V_tangente, I_tangente * 1000, color="purple", linewidth=2,
         label=f"Retta Tangente (r_d = {r_d:.2f} $\Omega$)")

# Evidenzio il punto di lavoro
plt.plot(V_Q, I_Q * 1000, 'ko', markersize=6)
plt.annotate(f'Q ({V_Q:.2f}V, {I_Q*1000:.1f}mA)',
             (V_Q, I_Q * 1000),
             textcoords="offset points",
             xytext=(-60, 10), ha='center', fontsize=10, fontweight='bold')

plt.ylim(0, max(I_carico * 1000) * 1.2)
plt.xlim(0.65, 0.8) # Zoom sulla zona di interesse per vedere meglio la tangente

plt.title("Punto di Lavoro e Resistenza Differenziale")
plt.xlabel('Tensione V_diodo [V]')
plt.ylabel('Corrente I_diodo [mA]')
plt.legend()
plt.grid(True)
plt.show()