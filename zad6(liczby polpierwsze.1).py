def czypierwsza(cyfra):
    if cyfra == 1:
        return False
    for i in range(2, cyfra):
        if cyfra % i == 0:
            return False
        if i * i > cyfra:
            break
    return True

def czypolpierwsza(n):
    if n == 1:
        print("To nie jest liczba półpierwsza.")
    else:
        dz = 2
        while n % dz > 0:
           dz += 1
        if czypierwsza(dz):
            if czypierwsza(int(n/dz)):
                print("To jest liczba półpierwsza")
            else:
                print("To nie jest liczba półpierwsza.")
        else:
            print("To nie jest liczba półpierwsza.")
czypolpierwsza(27)
