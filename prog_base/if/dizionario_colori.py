#Programma che utilizza un dizionario per tradurre i colori dall'italiano all'inglese

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

colore_in_italiano = input("inserire un colore: ")

if colore_italiano in colori:
  print("La traduzione di ", colore_in_italiano," in inglese è:", colori[colore_in_italiano])
else:
  print("Il colore ", colore_in_italiano, " non è presente nel dizionario.")

