from math import factorial

def binomial_coefficient(k, n):
	"""
		Return the number of way to choose
		k elements from a set of n elements.
	"""
	if (k > n):
		return None
	elif (k == n):
		return 1
	else:
		return (factorial(n)) // (factorial(k) * factorial(n-k))

def lattice_path(n):
	"""
		Return the number of possible lattice
		path from a square of a n x n size.
	"""
	if (n == 0):
		return 0
	return (binomial_coefficient(n, 2*n))

print({i:lattice_path(i) for i in range(21)})