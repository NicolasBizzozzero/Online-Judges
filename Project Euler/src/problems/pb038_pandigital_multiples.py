import itertools

from src.common.maths import length_int


def pandigital_multiples() -> dict:
    all_products = pandigital_multiples_reversed()

    return {
        "result": sum(all_products),
        "expected": 45228,
    }


def pandigital_multiples_bruteforce() -> set:
    all_products = set()
    for multiplicand in range(1, 10_000):
        for multiplier in range(multiplicand + 1, 10_000):
            product = multiplicand * multiplier
            digits = str(multiplicand) + str(multiplier) + str(product)

            if is_pandigital(int(digits)):
                all_products.add(product)
    return all_products


def pandigital_multiples_reversed() -> set:
    """Instead of computing every product for multiple ranges and check if they are pandigitals, we can reverse the
    problem and take every permutation of digits from 1-to-9 and check if they can result in a valid product.
    """
    all_products = set()
    for digits in itertools.permutations("123456789"):
        for idx_multiplier in range(2, 7):
            for idx_product in range(idx_multiplier + 1, 8):
                multiplicand = int("".join(digits[:idx_multiplier]))
                multiplier = int("".join(digits[idx_multiplier:idx_product]))
                product = int("".join(digits[idx_product:]))
                if multiplicand * multiplier == product:
                    all_products.add(product)
    return all_products


def is_pandigital(number: int) -> bool:
    if length_int(number) == 9:
        number = set(str(number))
        return len(number) == 9 and "0" not in number
    return False
