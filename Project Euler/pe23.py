from math import sqrt
from enum import Enum


def memoize(function: callable) -> callable:
    """ Caches a function's return value each time it is called.
        If called later with the same arguments, the cached value is returned.
    """
    cache = {}
    miss = object()

    def wrapper(*args, **kwargs):
        # If the result as already be calculated, it's a hit
        result = cache.get(args, miss)
        if result is miss:
            # Else, we call the original function and cache it's result
            result = function(*args, **kwargs)
            cache[args] = result
        return result
    return wrapper


def time_this(function: callable) -> callable:
    """ Print the execution time of the wrapped function. """
    def wrapper(*args, **kwargs):
        from time import time
        time_begin = time()
        result = function(*args, **kwargs)
        time_end = time()
        time_total = time_end - time_begin
        second_or_seconds = "second" if (time_total < 1) else "seconds"
        print("Execution time for \"{}\": {} {}".format(
            function.__name__, time_total, second_or_seconds))
        return result
    return wrapper


def is_divisible_by(n: int, divisor: int) -> bool:
    """ Return True if n is divisible by divisor, False otherwise. """
    return n % divisor == 0


def get_divisors_of(n: int, proper: bool = False) -> list:
    """ Return a list containing all the divisors of n. """
    if (n <= 0):
        n = abs(n)
    if proper:
        divisors = [1]
    else:
        divisors = [1, n]

    ceil = int(sqrt(n))
    for i in range(ceil, 2, -1):
        if is_divisible_by(n, i):
            divisors.append(i)
            divisors.append(n // i)
    return divisors


class NumberStatus(Enum):
    ABUNDANT = 0
    DEFICIENT = 1
    PERFECT = 2


def get_status(number: int) -> NumberStatus:
    divisors_value = sum(get_divisors_of(number, proper=True))
    if divisors_value > number:
        return NumberStatus.ABUNDANT
    elif divisors_value < number:
        return NumberStatus.DEFICIENT
    return NumberStatus.PERFECT


def is_perfect(number: int) -> bool:
    return sum(get_divisors_of(number, proper=True)) == number


def is_abundant(number: int) -> bool:
    return sum(get_divisors_of(number, proper=True)) > number


def is_deficient(number: int) -> bool:
    return sum(get_divisors_of(number, proper=True)) < number


def get_all_abundant_numbers(ceil: int, floor: int = 1) -> list:
    abundant_numbers = []
    for n in range(ceil, floor + 1):
        if is_abundant(n):
            abundant_numbers.append(n)
    return abundant_numbers


def main():
    abundant_numbers = get_all_abundant_numbers(ceil=1, floor=28123)
    for n in 28123, 28122:
        if n in abundant_numbers:
            print(n)
        elif is_abundant(n):
            print(n)
    can_be_written_as_the_sum_of_two_abundant_numbers = set()
    for i in range(len(abundant_numbers)):
        for j in range(i + 1, len(abundant_numbers)):
            if abundant_numbers[i] + abundant_numbers[j] <= 28123:
                can_be_written_as_the_sum_of_two_abundant_numbers.add(abundant_numbers[i] + abundant_numbers[j])
            else:
                break

    # Sum the number who CANNOT be written as a sum of two abundant numbers
    result = 0
    for i in range(1, 28124):
        if i not in can_be_written_as_the_sum_of_two_abundant_numbers:
            result += i

    print(result)


if __name__ == '__main__':
    main()
