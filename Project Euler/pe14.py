# -*- coding: utf-8 -*-

def collatzProblem(n, dico):
    iterations = 0

    while n != 1:
        # Cas où on connait deja le nombre d'iterations à partir de n
        try:
            return dico[n] + iterations
        except:
            KeyError
    
        iterations += 1

        # Calcul de la nouvelle valeur de n
        if not (n%2):
            n = n/2
        else:
            n = (3*n)+1

    return iterations

rankMax = 0
iterationMax = 0
dico = dict()
for i in range(1, 1000000):
    nbOfIterations = collatzProblem(i, dico)
    dico[i] = nbOfIterations
    if nbOfIterations > iterationMax:
        iterationMax = nbOfIterations
        rankMax = i

print(rankMax)
input()

