import random

sugeneguotas = random.randint(1, 101)
spejimai = 0
while True:
    spejimas = int(input("Spėkite skaičių nuo 0 iki 100: "))
    spejimai += 1
    if spejimas > sugeneguotas:
        print("Mažiau")
    if spejimas < sugeneguotas:
        print("Daugiau")
    if spejimas == sugeneguotas:
        print(f"Atspėjote! Skaičius - {sugeneguotas}")
        print(f"Spėjimai - {spejimai}")
        break
