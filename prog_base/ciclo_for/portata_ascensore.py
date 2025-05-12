peso_max = int(input("inserire il peso massimo ammesso per l'ascensore: "))

peso_persone = 0

for i in range(1, 5):
    print("Inserire il peso della persona", i)
    x = int(input())
    peso_persone = peso_persone + x

if peso_persone > peso_max:
    print("Arresto di sicurezza")
else:
    print("Partenza OK!")
