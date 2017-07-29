for a in range(1001):
    for b in range(a+1, 1001):
        for c in range(b+1, 1001):
            if (a**2 + b**2 == c**2):
                if (a+b+c == 1000):
                    print(str(a), str(b), str(c))
                    print(str(a*b*c))
                    break

input()