def czyzaprzyjanione(n1, n2):
    dz1 = 0
    dz2 = 0
    for i in range(1, n1):
        if n1 % i == 0:
            dz1 += i
        else:
            pass
    for i in range(1, n2):
        if n2 % i == 0:
            dz2 += i
        else:
            pass
    if n1 == dz2 and n2 == dz1:
        print("Jest to para liczb zaprzyjaznionych.")
    else:
        print("Nie jest to para liczb zaprzyjaznionych.")

czyzaprzyjanione(220, 284)