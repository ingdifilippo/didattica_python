import random

lista_allievi = ["Alice", "Marco", "Carlo", "David", "Eva", "Franco", "Grazia", "Enrico", "Asia", "Mirko"]

for allievo in lista_allievi:
    print(allievo)

allievo_estratto = random.choice(lista_allievi)

print("L'allievo estratto casualmente è:" allievo_estratto)

lista_allievi.remove(allievo_estratto)

for allievo in lista_allievi:
    print(allievo)
