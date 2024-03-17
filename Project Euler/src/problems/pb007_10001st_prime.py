from src.common.maths import prime


def ten_thousand_first_prime(number: int = 10001) -> dict:
    return {
        "result": prime(number),
        "expected": 104743,
    }
