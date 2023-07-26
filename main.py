import random

sugeneguotas = random.randint(1, 101)
print(sugeneguotas)
while True:
    spejimas = int(input("Spėkite skaičių: "))
    if spejimas > sugeneguotas:
        print("Mažiau")
    if spejimas < sugeneguotas:
        print("Daugiau")