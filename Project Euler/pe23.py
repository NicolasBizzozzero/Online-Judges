def get_divisors_of(n):
  pass
  
def get_sum_of_divisors_of(n):
  return sum(get_divisors_of(n))

def is_perfect(n):
  return (get_sum_of_divisors_of(n)-n == n)

def is_deficient(n):
  return (get_sum_of_divisors_of(n)-n < n)
 
def is_abundant(n):
  return (get_sum_of_divisors_of(n)-n > n)

if __name__ == "__main__":
  sum = 0
  for number in range(1, 28124):
    pass