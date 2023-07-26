import random

print("Įveskite spėjamo skaičiaus diapazoną: ")
nuo = int(input("Nuo: "))
iki = int(input("Iki: "))
sugeneguotas = random.randint(nuo, iki)
spejimai = 0
while True:
    spejimas = int(input(f"Spėkite skaičių nuo {nuo} iki {iki}: "))
    spejimai += 1
    if spejimas > sugeneguotas:
        print("Mažiau")
    if spejimas < sugeneguotas:
        print("Daugiau")
    if spejimas == sugeneguotas:
        print(f"Atspėjote! Skaičius - {sugeneguotas}")
        print(f"Spėjimai - {spejimai}")
        break
