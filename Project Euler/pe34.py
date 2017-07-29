from math import factorial

factorials = {i:factorial(i) for i in range(10)}

def get_factorial_of(n):
  return factorials[n]

def get_sum_of_factorials_of(n):
  sum = 0
  for digit in str(n):
    sum += get_factorial_of(int(digit))
  return sum

if __name__ == "__main__":
  numb = set()
  ceil = (9 * factorials[9])+1 # Verify this ceil
  for n in range(3, ceil):
    if get_sum_of_factorials_of(n) == n:
      numb.add(n)
  print(sum(numb))