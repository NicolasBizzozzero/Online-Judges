import functools
import math
from collections import defaultdict, Counter


def is_odd(number: int) -> bool:
    return number % 2 == 1


def is_even(number: int) -> bool:
    return number % 2 == 0


def is_divisible_by(number: int, divisor: int) -> bool:
    return number % divisor == 0


def length_int(number: int) -> int:
    return int(math.log10(number)) + 1


@functools.lru_cache
def fibonacci(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def is_prime(n: int) -> bool:
    if n == 1:
        return False
    if n < 4:
        return True  # 2 and 3 ar prime
    if is_even(n):
        return False
    if n < 9:
        return True  # We have already excluded 4, 6 and 8.
    if is_divisible_by(n, 3):
        return False

    # Cas général
    f = 5
    while f <= math.floor(math.sqrt(n)):
        if is_divisible_by(n, f):
            return False
        if is_divisible_by(n, f + 2):
            return False
        f += 6
    return True


def is_palindromic(number: int) -> bool:
    return str(number) == str(number)[::-1]


def prime(number: int) -> int:
    """Get the nth prime number."""
    if number <= 0:
        raise ValueError(number)

    if number == 1:
        return 2

    current_number = 1
    i = 1
    while current_number < number:
        i += 2
        if is_prime(i):
            current_number += 1
    return i


def lcm(*numbers: int) -> int:
    max_exposants = defaultdict(int)
    for multiple in numbers:
        factors = prime_factors(multiple)
        for exposant, count in Counter(factors).items():
            max_exposants[exposant] = max(count, max_exposants[exposant])

    # Recompose number with the proper exposants
    number = 1
    for exposant, count in max_exposants.items():
        number *= exposant**count

    return number


def prime_factors(n: int) -> list[int]:
    """Decompose a number into a product of prime factors."""
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


def triangle_number(n: int) -> int:
    return (n * (n + 1)) // 2


def divisors_of(n: int) -> list[int]:
    divisors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if is_divisible_by(n, i):
            divisors.append(i)
            if i * i != n:
                divisors.append(n // i)
    return sorted(divisors)
