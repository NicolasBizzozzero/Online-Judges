from pymath import fibonacci


def P(n, k):
	"""
		Return 1 if n can be written as the sum
		of k prime numbers, 0 otherwise. 
		Examples :
		P(10, 2) = 1
		P(11, 2) = 0
	"""
	pass

  
def S(n):
	"""
		Return the sum of all P(i, k) over
		1 <= i, k <= n
		Examples :
		S(10) = 20
		S(100) = 2402
		S(1000) = 248838
	"""
	total = 0
	for i in range(1, n+1):
		for k in range(1, i):
			total += P(i, k)
	return total


def main():
	list_F_k = []
	for k in range(3, 45):
		list_F_k.append(fibonacci(k))

	list_S_F_k = []
	for fibonacci_number in list_F_k:
		list_S_F_k.append(S(fibonacci_number))
  
	answer = sum(list_S_F_k)
	print(str(answer))

if __name__ == "__main__":
	print(str(fibonacci(44)))
	print("P(10, 2) =", str(P(10, 2)))
	print("P(11, 2) =", str(P(11, 2)))