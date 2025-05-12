#distanza_terra_luna = 384400000  # metri (distanza media Terra-Luna)
#distanza_sole_terra = 149600000000  # metri (distanza media Sole-Terra)

distanza_metri = float(input("Inserisci la distanza in metri da A a B: "))

velocita_luce = 299792458  # metri al secondo
tempo_percorrenza_secondi = distanza_metri / velocita_luce

print("La luce impiega ", tempo_percorrenza_secondi, " secondi per raggiungere la Luna dalla Terra.")

#Conversione del tempo in minuti

tempo_percorrenza_minuti = tempo_percorrenza_secondi / 60
print(f"Questo equivale a circa", tempo_percorrenza_minuti, " minuti.")
