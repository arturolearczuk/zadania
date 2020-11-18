def rozloz(liczba):
    dz = 2

    while liczba > 1:
        while liczba % dz == 0:
            print(f"{liczba}  {dz}")
            liczba = liczba // dz
        dz += 1

print("Podaj zakres Liczb jakich chcesz rozłożyc na czynniki")
x = int(input("Od: "))
y = int(input("Do: ")) 

for i in range(x, y):
    print(f"Rozkład {i}")
    (rozloz(i))