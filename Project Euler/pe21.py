from math import sqrt


def timeit(function):
    def wrapper(*args):
        from time import time
        beginning = time()
        result = function(*args)
        end = time()
        print(function.__name__, ":", str(end - beginning), "seconds")
        return result
    return wrapper


def memoize(function):
    results = {}

    def wrapper(*args):
        if args in results.keys():
            return results[args]
        else:
            results[args] = function(*args)
            return results[args]
    return wrapper


def is_divisible(n: int, divisor: int) -> bool:
    return n % divisor == 0


def are_amicables(a: int, b: int) -> bool:
    return a != b and sum(get_divisors(b)) == a and sum(get_divisors(a)) == b


def is_amicable(n: int) -> int:
    sum_divisors = sum(get_divisors(n))
    if n == sum_divisors:
        return None
    if n != sum(get_divisors(sum_divisors)):
        return None
    return sum_divisors


@memoize
def get_divisors(n: int) -> set:
    divisors = set()
    divisors.add(1)

    if is_divisible(n, 2):
        divisors.add(2)
        divisors.add(n // 2)
    divisor = 3
    floor = sqrt(n)
    while divisor < floor:
        if is_divisible(n, divisor):
            divisors.add(divisor)
            divisors.add(n // divisor)
        divisor += 1
    return divisors


@timeit
def main():
    amicable_numbers = set()
    for n in range(1, 10001):
        if n in amicable_numbers:
            continue
        s_divisors = is_amicable(n)
        if s_divisors:
            amicable_numbers.add(n)
            amicable_numbers.add(s_divisors)
    print(sum(amicable_numbers))


if __name__ == "__main__":
    main()
