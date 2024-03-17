from src.common.iterators import iter_primes


def summation_of_primes() -> dict:
    summation = 0
    for prime in iter_primes():
        if prime >= 2_000_000:
            break
        summation += prime
    return {
        "result": summation,
        "expected": 142913828922,
    }
