def fibonacci(n, dico):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return dico[n-1] + dico[n-2]

dico = {0:0, 1:1, 2:1}
numberOfDigits = 0
n = 0
while numberOfDigits < 1000:
    n += 1
    fiboNumber = fibonacci(n, dico)
    dico[n] = fiboNumber
    numberOfDigits = len(str(fiboNumber))

print(n)
input()