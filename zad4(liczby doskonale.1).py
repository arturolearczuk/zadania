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
        print(f"{n} jest liczbą doskonałą")
    else:
        print(f"{n} nie jest liczbą doskonałą")

x = (int(input("Podaj liczbe którą chcez sprawdzić czy jest liczbą doskonałą: ")))

czy_doskonala(x)