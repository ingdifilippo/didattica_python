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
R = 220.0  # Resistenza di limitazione [Ohm]
# Valori di Vcc: limite inferiore (4V), nominale (5V), limite superiore (6V)
Vcc_values = [4.0, 5.0, 6.0]

# Stili delle linee corrispondenti ai valori di Vcc (continuo, tratteggiato, continuo)
line_styles = ['-', '--', '-']
# Colori per distinguere le rette
line_colors = ['green', 'blue', 'red']

V_start = 0
V_stop = 0.8  # Aumentato leggermente per inquadrare meglio l'incrocio a 6V
punti_di_calcolo = 1000

# Sequenza di tensioni per l'asse X
V_diodo = np.linspace(V_start, V_stop, punti_di_calcolo)

# 1. Calcolo la corrente del diodo (Curva)
I_diodo = I_sat * np.exp(V_diodo / V_termica)

# Preparo la figura
plt.figure(figsize=(10, 7))

# Traccio la curva del diodo
plt.plot(V_diodo, I_diodo * 1000, color="orange", linewidth=2.5, label="Caratteristica Diodo")

print("--- Punti di Lavoro (Q-Points) con Ripple ---")

# 2. Itero sui valori di Vcc per calcolare e disegnare rette e punti di lavoro
for vcc, stile, colore in zip(Vcc_values, line_styles, line_colors):
    # Retta di carico per il Vcc corrente
    I_carico = (vcc - V_diodo) / R


    # Funzione per l'intersezione (nota: passiamo vcc come parametro addizionale)
    def eq_intersezione(V, v_alim):
        return I_sat * np.exp(V / V_termica) - (v_alim - V) / R


    # Trovo il Q-Point passando il valore corrente di vcc ad args
    V_Q = fsolve(eq_intersezione, 0.7, args=(vcc,))[0]
    I_Q = (vcc - V_Q) / R

    print(f"Vcc = {vcc}V -> V_Q = {V_Q:.4f} V, I_Q = {I_Q * 1000:.2f} mA")

    # Traccio la retta di carico con lo stile richiesto
    plt.plot(V_diodo, I_carico * 1000, color=colore, linestyle=stile, linewidth=1.5,
             label=f"Retta di Carico (Vcc={vcc}V)")

    # Evidenzio il punto di lavoro
    plt.plot(V_Q, I_Q * 1000, 'ko', markersize=6)  # 'ko' = pallino nero

    # Aggiungo un'etichetta di testo vicino a ogni pallino
    plt.annotate(f'Q ({V_Q:.2f}V, {I_Q * 1000:.1f}mA)',
                 (V_Q, I_Q * 1000),
                 textcoords="offset points",
                 xytext=(10, +5),  # Sposta il testo un po' a destra e in basso rispetto al punto
                 ha='left', fontsize=9)

# 3. Dettagli estetici del grafico
# Imposto il limite Y basandomi sulla retta più alta (6V) a V=0 per inquadrare tutto
ymax = (max(Vcc_values) / R) * 1000
plt.ylim(0, ymax * 1.1)
plt.xlim(0, V_stop)

plt.title("Analisi del Punto di Lavoro (Q-Point) con Ripple di Tensione (±1V)")
plt.xlabel('Tensione V_diodo [V]')
plt.ylabel('Corrente I_diodo [mA]')
plt.legend()
plt.grid(True)
plt.show()