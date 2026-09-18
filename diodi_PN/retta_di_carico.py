import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

# Calcolo della tensione termica
q = 1.602E-19
T = 300
k_boltzman = 1.38E-23

V_termica = k_boltzman * T / q
print("V_T=", V_termica)

I_sat = 1E-14

# Parametri del circuito (Aggiunti)
V_cc = 5.0  # Tensione di alimentazione [V]
R = 220.0   # Resistenza di limitazione [Ohm]

V_start = 0
V_stop = 0.77
punti_di_calcolo = 1000

# Creo una sequenza di mille valori di tensione per l'asse X
V_diodo = np.linspace(V_start, V_stop, punti_di_calcolo)

# 1. Calcolo la corrente del diodo (Curva)
I_diodo = I_sat * np.exp(V_diodo / V_termica)

# 2. Calcolo la corrente della retta di carico (Retta)
I_carico = (V_cc - V_diodo) / R

# 3. Ricerca del Punto di Lavoro (Q-Point)
# Definisco una funzione che rappresenta la differenza tra le due correnti
# L'intersezione si ha quando questa differenza è zero.
def eq_intersezione(V):
    return I_sat * np.exp(V / V_termica) - (V_cc - V) / R

# Uso fsolve per trovare lo zero della funzione, partendo da un'ipotesi di 0.7V
V_Q = fsolve(eq_intersezione, 0.7)[0]
I_Q = (V_cc - V_Q) / R

print(f"\n--- Punto di Lavoro (Q-Point) ---")
print(f"Tensione V_Q = {V_Q:.4f} V")
print(f"Corrente I_Q = {I_Q*1000:.4f} mA\n")


# 4. Disegno il grafico
plt.figure(figsize=(8, 6))

# Traccio la curva del diodo
plt.plot(V_diodo, I_diodo * 1000, color="orange", linewidth=2, label="Caratteristica Diodo")


# Creo una sequenza di mille valori di tensione per l'asse X
V = np.linspace(V_start, 5, punti_di_calcolo)
# 2. Calcolo la corrente della retta di carico (Retta)
I_carico = (V_cc - V) / R

# Traccio la retta di carico
plt.plot(V, I_carico * 1000, color="blue", linewidth=2, label="Retta di Carico")

# Evidenzio il punto di lavoro con un pallino rosso
etichetta_Q = f'Punto di Lavoro (Q)\n({V_Q:.2f} V, {I_Q*1000:.1f} mA)'
plt.plot(V_Q, I_Q * 1000, 'ro', markersize=8, label=etichetta_Q)

# Imposto i limiti dell'asse Y per inquadrare bene l'intersezione
# ed escludere i valori troppo alti dell'esponenziale a destra del grafico
plt.ylim(0, max(I_carico * 1000) * 1.5)

# Dettagli estetici
plt.title("Caratteristica Diodo e Retta di Carico")
plt.xlabel('Tensione V_diodo [V]')
plt.ylabel('Corrente I_diodo [mA]')
plt.legend()
plt.grid(True)
plt.show()
