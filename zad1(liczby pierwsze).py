def sprawdz(cyfra):
    for i in range(2, cyfra):
        if cyfra % i == 0:
            return False
        if i * i > cyfra:
            break
    return True
print("Podaj zakres sprawdzania liczb pierwszych")
x = int(input("Od: "))
y = int(input("Do: "))

for i in range(x, y):
    if sprawdz(i):
        print(i)
    else:
        pass