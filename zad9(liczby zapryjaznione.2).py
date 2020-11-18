def znajdzpary(x,y):
    pary = []
    sumy = []
    for n1 in range(x, y):
        s = 0
        for i in range(1, n1):
            if n1 % i == 0:
                s += i
            else:
                pass
        sumy.append(s)
    for ndz in range( y-x ):
        if sumy[ndz] == 1:
            pass
        else:
            for n2 in range(x, y):
                s = 0
                for i in range(1, n2):
                    if n2 % i == 0:
                        s += i
                    else:
                        pass
                if ndz + x == s and n2 == sumy[ndz] and ndz + x != n2:
                    if (f"{n2}:{ndz + x}") in pary:
                        pass
                    else:
                        pary.append(f"{ndz + x}:{n2}")
                else:
                    pass
    print(pary)           

                

znajdzpary(1,3000)
 