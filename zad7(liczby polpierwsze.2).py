def czypierwsza(cyfra):
    if cyfra == 1:
        return False
    for i in range(2, cyfra):
        if cyfra % i == 0:
            return False
        if i * i > cyfra:
            break
    return True

def znajdztrojki(od, do):
    polpierwsze = []
    trojki = []
    for n in range(od,do): 
        if n == 1 or 0:
            pass
        else:
            dz = 2
            while n % dz > 0:
               dz += 1
            if czypierwsza(dz):
                if czypierwsza(int(n/dz)):
                    polpierwsze.append(n)
                else:
                    pass
            else:
                pass
    for i in range(len(polpierwsze)):
        if polpierwsze[i] == polpierwsze[-1]:
            pass
        elif polpierwsze[i] == polpierwsze[i - 1] + 1 and polpierwsze[i] == polpierwsze[i + 1] - 1:
            trojki.append(f"{polpierwsze[i - 1]}:{polpierwsze[i]}:{polpierwsze[i + 1]}")
        else:
            pass
    print(trojki)

znajdztrojki(1,1000)