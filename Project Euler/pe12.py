from math import sqrt, floor

def get_triangle_number(n):
	"""
		A triangle number is a number who has for value the sum
		of the n first positives integers.
		This function return the n-th triangle number.
	"""
	return (n*(n+1))//2

def get_divisors_of(n):
	""" Return a set containing all the divisors of n. """
	if (n <= 0):
		return 0
	divisors = set()
	divisors.add(1)
	divisors.add(n)
	ceil = int(sqrt(n))#int(floor(sqrt(n)))
	for i in range(ceil, 1, -1):
		if (n%i == 0):
			divisors.add(i)
			divisors.add(n//i)
	return divisors

def get_number_of_divisors_of(n):
	if (n <= 0):
		return 0
	numberOfDivisors = 2
	ceil = int(sqrt(n))#int(floor(sqrt(n)))
	for i in range(ceil, 1, -1):
		if (n%i == 0):
			numberOfDivisors += 2
	return numberOfDivisors

if __name__ == '__main__':
	dictionaryOfTriangleNumbers = {0:0}
	numberOfDivisors = 0
	currentMaxTriangleNumber = 0
	while (numberOfDivisors < 500):
		currentMaxTriangleNumber += 1
		valueOfMaxTriangleNumber = get_triangle_number(currentMaxTriangleNumber)
		numberOfDivisors = get_number_of_divisors_of(valueOfMaxTriangleNumber)

	print(str(valueOfMaxTriangleNumber))