#Programma che utilizza un dizionario per tradurre i colori dall'italiano all'inglese
#I dizionari sono strutture di tipo nome:valore in cui posso recuperare i valori 
#tramite nome_dizionario[nome_elemento]

colori = {
        "rosso"    : "red",
        "blu"      : "blue",
        "verde"    : "green",
        "giallo"   : "yellow",
        "arancione": "orange",
        "viola"    : "purple",
        "marrone"  : "brown",
        "nero"     : "black",
        "bianco"   : "white",
        "grigio"   : "grey"
    }

print("Benvenuto nel traduttore di colori!")
print("Inserisci un colore in italiano (o 'esci' per terminare).")

#ciclo infinito
while True:
    colore_italiano = input("Colore: ")
    if colore_italiano == "esci":
        print("Grazie per aver usato il traduttore di colori!")
        break
    elif colore_italiano in colori:
        print("La traduzione di ", colore_italiano," in inglese è:", colori[colore_italiano])
    else:
        print("Il colore ", colore_italiano, " non è presente nel dizionario.")

