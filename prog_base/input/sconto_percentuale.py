# Inserimento del prezzo del prodotto
prezzo_prodotto = float(input("Inserisci il prezzo del prodotto: "))

# Inserimento dello sconto percentuale
sconto_percentuale = float(input("Inserisci lo sconto percentuale: "))

# Calcolo dello sconto in valore assoluto
sconto_valore = (sconto_percentuale / 100) * prezzo_prodotto

# Calcolo del prezzo finale
prezzo_finale = prezzo_prodotto - sconto_valore

# Calcolo del risparmio
risparmio = prezzo_prodotto - prezzo_finale

# Stampa dei risultati
print("Prezzo originale:", prezzo_prodotto)
print("Sconto percentuale:", sconto_percentuale, "%")
print("Sconto in valore assoluto:", sconto_valore)
print("Prezzo finale:", prezzo_finale)
print("Risparmio:", risparmio)
