resistivita = {  "argento"   : 0.0164,
                 "rame"      : 0.0175,
                 "oro"       : 0.024,
                 "alluminio" : 0.029,
                 "tungsteno" : 0.055,
                 "stagno"    : 0.12,
                 "ferro"     : 0.1,
                 "piombo"    : 0.206,
                 "manganina" : 0.4,
                 "costantana": 0.5,
                 "mercurio"  : 0.955,
                 "carbone"   : 30,
                 "germanio"  : 5e5,
                 "silicio"   : 25e6
                 }

materiale = input("Inserire il materiale del filo: ")

if materiale in resistivita:
    print("la resistività del materiale ", materiale, "risulta", resistivita[materiale], "Ohm")
else:
    print("materiale non presente in tabella")
