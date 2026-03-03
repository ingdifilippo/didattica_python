import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# --- Parametri del Circuito ---
E = 12  # Tensione [V]
R = 1000  # Resistenza [Ohm]
C = 1e-6  # Capacità [F]
tau = R * C  # Costante di tempo
t_max = 5 * tau  # Durata totale del transitorio da mostrare

# --- Setup della Figura ---
fig, ax1 = plt.subplots(figsize=(10, 6))
ax2 = ax1.twinx()

# Limiti degli assi
ax1.set_xlim(0, t_max)
ax1.set_ylim(-0.5, E + 1)
ax2.set_ylim(-0.0001, (E / R) + 0.0002)

ax1.set_xlabel('Tempo (s)')
ax1.set_ylabel('Tensione V_c (V)', color='blue')
ax2.set_ylabel('Corrente i (A)', color='green')
plt.title('Animazione Transitorio di Carica RC')

# Linee vuote che verranno aggiornate
line_v, = ax1.plot([], [], 'b-', lw=2, label='Tensione V_c')
line_i, = ax2.plot([], [], 'g--', lw=2, label='Corrente i')
point_v, = ax1.plot([], [], 'bo')  # Pallina che segue la tensione
point_i, = ax2.plot([], [], 'ro')  # Pallina che segue la corrente


# Funzione di inizializzazione
def init():
    line_v.set_data([], [])
    line_i.set_data([], [])
    point_v.set_data([], [])
    point_i.set_data([], [])
    return line_v, line_i, point_v, point_i


# Funzione di animazione (chiamata per ogni frame)
def update(frame):
    # 'frame' rappresenta il tempo corrente da 0 a t_max
    curr_t = frame
    curr_v = E * (1 - np.exp(-curr_t / tau))
    curr_i = (E / R) * np.exp(-curr_t / tau)

    # Dati storici fino al frame attuale per disegnare la linea
    t_history = np.linspace(0, curr_t, 100)
    v_history = E * (1 - np.exp(-t_history / tau))
    i_history = (E / R) * np.exp(-t_history / tau)

    line_v.set_data(t_history, v_history)
    line_i.set_data(t_history, i_history)
    point_v.set_data([curr_t], [curr_v])
    point_i.set_data([curr_t], [curr_i])

    return line_v, line_i, point_v, point_i


# Creazione animazione
# frames: quanti punti calcolare; interval: ritardo tra frame in ms
# Per durare circa 10 secondi con 200 frame, usiamo interval=50ms
ani = FuncAnimation(fig, update, frames=np.linspace(0, t_max, 200),
                    init_func=init, blit=True, interval=50, repeat=False)

ax1.grid(True, linestyle=':', alpha=0.7)
plt.show()
