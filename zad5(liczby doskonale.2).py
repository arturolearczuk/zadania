def czy_doskonala(n):
    dz = 1
    dzielniki = []

    while dz <= (n / 2):
        if n % dz == 0:
            dzielniki.append(dz)
            dz += 1
        else:
            dz += 1

    n1 = 0

    for i in range(len(dzielniki)):
        n1 += dzielniki[i]
    
    if n1 == n:
        return (n)

print("Podaj zakras aby znaleźć liczby doskonałe")
x = int(input("Od:"))
y = int(input("Do:"))

for i in range(x, y):
    if czy_doskonala(i):
        print(i)
    else:
        pass