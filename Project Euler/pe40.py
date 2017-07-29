string = ""
for i in range(1000001):
    string += str(i)

product = 1
for i in [1, 10, 100, 1000, 10000, 100000, 1000000]:
    product *= int(string[i])
    
print(product) 