# Author : BIZZOZZERO Nicolas
# Completed on Sun, 24 Jan 2016, 22:38
#
# This program find the solution of the problem 1 of the Project Euler.
# The problem is the following :
#
# If we list all the natural numbers below 10 that are multiples of 3 or
# 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
#
# The answer to this problem is :
# 233168


def is_divisible_by(n: int, divisor: int) -> bool:
    """Return True if n is divisible by divisor, False otherwise. """
    return n % divisor == 0


def main():
    set_of_multiples = set()
    for i in range(1001):
        if is_divisible_by(i, 3) or is_divisible_by(i, 5):
            set_of_multiples.add(i)
    print(sum(set_of_multiples))


if __name__ == '__main__':
    main()
