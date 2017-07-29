# Author : BIZZOZZERO Nicolas
# Completed on Sun, 24 Jan 2016, 22:49
#
# This program find the solution of the problem 3 of the Project Euler.
# The problem is the following :
#
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
#
# The answer to this problem is :
# 6857

from math import sqrt


def is_divisible_by(n: int, divisor: int) -> bool:
    """Return True if n is divisible by divisor, False otherwise. """
    return n % divisor == 0


def main():
    n = 600851475143
    m = 1
    largest_prime_factor = 1
    while sqrt(m) < n:
        if is_divisible_by(n, m):
            n /= m
            largest_prime_factor = m
        m += 2
    print(largest_prime_factor)


if __name__ == '__main__':
    main()
