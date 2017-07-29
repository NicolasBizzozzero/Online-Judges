pow_of_5th = {i:i**5 for i in range(10)}

def get_5th_pow_of(n):
  return pow_of_5th[n]

def get_sum_of_5th_pow_of(n):
  sum = 0
  for digit in str(n):
    sum += get_5th_pow_of(int(digit))
  return sum

if __name__ == "__main__":
  numb = set()
  ceil = ((pow_of_5th[9]) * 9)+1 # Verify this ceil
  for n in range(2, ceil):
    if get_sum_of_5th_pow_of(n) == n:
      numb.add(n)
  print(sum(numb))