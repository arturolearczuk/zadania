def sprawdz(cyfra):
    for i in range(2, cyfra):
        if cyfra % i == 0:
            return False
        if i * i > cyfra:
            break
    return True

pierwsze = []
x = int(input("Od: "))
y = int(input("Do: "))

for i in range(x, y):
    if sprawdz(i):
        pierwsze.append(i)
    else:
        pass

for i in range(len(pierwsze)):
    if pierwsze[i] - pierwsze[i - 1] == 2:
        print(f"{pierwsze[i - 1]} {pierwsze[i]}")
    else:
        pass