# Author : BIZZOZZERO Nicolas
# Completed on Sun, 24 Jan 2016, 23:03
#
# This program find the solution of the problem 4 of the Project Euler.
# The problem is the following :
#
# A palindromic number reads the same both ways. The largest palindrome made
# from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.
#
# The answer to this problem is :
# 906609


def is_a_palindrome(string: str) -> bool:
    """Return True if string is a palindrome, False otherwise.
        A palindrome is a string who can be read the same both
        ways.
    """
    return string == ''.join(reversed(string))


def is_a_palindromic_number(n: int) -> bool:
    """Return True if n is a palindromic number, False otherwise.
        A palindromic number is a number whose digits can be read
        the same both ways.
    """
    return is_a_palindrome(str(n))


def main():
    largest_palindrome = 0
    a = 999
    while a >= 100:
        b = 999
        while b >= a:
            if a * b <= largest_palindrome:
                break  # Since a * b is always going to be too small
            if is_a_palindromic_number(a * b):
                largest_palindrome = a * b
            b -= 1
        a -= 1
    print(largest_palindrome)


if __name__ == '__main__':
    main()
