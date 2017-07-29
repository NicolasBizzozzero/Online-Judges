from math import factorial

n = str(factorial(1000))
sum = 0
for digit in n:
  sum += int(digit)

print(sum)