peso_max = int(input("inserire il peso massimo ammesso per l'ascensore: "))

peso = 0

for i in range(1, 5):
    print("Inserire il peso della persona", i)
    x = int(input())
    peso = peso + x

if peso > peso_max:
    print("Arresto di sicurezza")
else:
    print("Partenza OK!")
