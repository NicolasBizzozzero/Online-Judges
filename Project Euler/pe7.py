# Author : BIZZOZZERO Nicolas
# Completed on Sun, 24 Jan 2016, 23:31

#
# This program find the solution of the problem 7 of the Project Euler.
# The problem is the following :
#
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we
# can see that the 6th prime is 13.
# What is the 10 001st prime number?
#
# The answer to this problem is :
# 104743


def getline(file: str, line_number: int) -> str:
    """Return the content of file at the line
        indicated by line_number.
    """
    counter = 0
    with open(file, 'r') as file:
        for line in file:
            counter += 1
            if counter == line_number:
                return line
    # If we are here, then the file has a number of lines inferior
    # to line_number
    return ""


def main():
    prime = getline(r"W:\vrac\primes.txt", 10001)
    print(prime)


if __name__ == '__main__':
    main()
