# Author : BIZZOZZERO Nicolas
# Completed on Sun, 24 Jan 2016, 23:11
#
# This program find the solution of the problem 5 of the Project Euler.
# The problem is the following :
#
# 2520 is the smallest number that can be divided by each of the
# numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible
# by all of the numbers from 1 to 20?
#
# The answer to this problem is :
# 232792560

# The easiest solution is to print 2*2*2*2*3*3*5*7*11*13*17*19
# But here's the bruteforce method


def isEvenlyDivisibleByAllTheNumbersFrom1To20(n):
    for i in range(1, 21):
        if n % i:
            return False
    return True


def main():
    i = 1
    while 1:
        print(i)
        if isEvenlyDivisibleByAllTheNumbersFrom1To20(i):
            print(i)
            break
        i += 1


if __name__ == '__main__':
    print(2 * 2 * 2 * 2 * 3 * 3 * 5 * 7 * 11 * 13 * 17 * 19)
