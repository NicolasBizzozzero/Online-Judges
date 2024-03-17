import math


def largest_prime_factor(max_number: int = 600_851_475_143) -> dict:
    prime_factors = []
    for number in range(1, int(math.sqrt(max_number)) + 1):
        if math.gcd(number, max_number) != 1:
            for prime in prime_factors:
                if math.gcd(prime, number) != 1:
                    break
            else:
                prime_factors.append(number)
    return {
        "result": prime_factors[-1],
        "expected": 6857,
    }
