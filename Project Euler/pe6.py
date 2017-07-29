# Author : BIZZOZZERO Nicolas
# Completed on Sun, 24 Jan 2016, 23:16

#
# This program find the solution of the problem 6 of the Project Euler.
# The problem is the following :
#
# The sum of the squares of the first ten natural numbers is,
# 1² + 2² + ... + 10² = 385
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)² = 552 = 3025
# Hence the difference between the sum of the squares of the first
# ten natural numbers and the square of the sum is 3025 − 385 = 2640.
# Find the difference between the sum of the squares of the first
# one hundred natural numbers and the square of the sum.
#
# The answer to this problem is :
# 25164150


def sum_of_the_square_of_the_n_first_numbers(n: int) -> int:
    return (((2 * n) + 1) * (n + 1) * n) // 6


def square_of_the_sum_of_the_n_first_numbers(n: int) -> int:
    sum = (n * (n + 1)) // 2
    return sum * sum


def main():
    print(
        square_of_the_sum_of_the_n_first_numbers(100) -
        sum_of_the_square_of_the_n_first_numbers(100))


if __name__ == '__main__':
    main()
