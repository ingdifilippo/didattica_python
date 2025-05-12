# Calcolo della distanza tra due punti nel piano cartesiano

# Richiedi all'utente di inserire le coordinate del primo punto
print("Inserisci le coordinate del primo punto:")
x1 = float(input("x1: "))  # Legge la coordinata x del primo punto e la converte in float
y1 = float(input("y1: "))  # Legge la coordinata y del primo punto e la converte in float

# Richiedi all'utente di inserire le coordinate del secondo punto
print("Inserisci le coordinate del secondo punto:")
x2 = float(input("x2: "))  # Legge la coordinata x del secondo punto e la converte in float
y2 = float(input("y2: "))  # Legge la coordinata y del secondo punto e la converte in float

# Calcola la differenza tra le coordinate x e y
delta_x = x2 - x1  # Calcola la differenza tra le coordinate x
delta_y = y2 - y1  # Calcola la differenza tra le coordinate y

# Calcola il quadrato delle differenze
delta_x_quadrato = delta_x * delta_x  # Calcola il quadrato della differenza tra le x
delta_y_quadrato = delta_y * delta_y  # Calcola il quadrato della differenza tra le y

# Calcola la somma dei quadrati
somma_quadrati = delta_x_quadrato + delta_y_quadrato  # Somma i quadrati delle differenze

# Calcola la radice quadrata della somma per ottenere la distanza
#  Poiché non possiamo usare la funzione math.sqrt(), usiamo l'elevamento a potenza 0.5
distanza = somma_quadrati ** 0.5  # Calcola la radice quadrata usando l'operatore di potenza

# Stampa il risultato
print("La distanza tra i due punti è:", distanza)  # Stampa la distanza calcolata
