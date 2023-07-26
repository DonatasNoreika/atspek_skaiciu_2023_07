import random

print("Įveskite spėjamo skaičiaus diapazoną: ")
nuo = int(input("Nuo: "))
iki = int(input("Iki: "))
spejamas_nuo = nuo
spejamas_iki = iki
sugeneguotas = random.randint(nuo, iki)
spejimai = 0
while True:
    spejimas = int(input(f"Spėkite skaičių nuo {spejamas_nuo} iki {spejamas_iki}: "))
    spejimai += 1
    if spejimas > sugeneguotas:
        spejamas_iki = spejimas
        print("Mažiau")
    if spejimas < sugeneguotas:
        spejamas_nuo = spejimas
        print("Daugiau")
    if spejimas == sugeneguotas:
        print(f"Atspėjote! Skaičius - {sugeneguotas}")
        print(f"Spėjimai - {spejimai}")
        break
