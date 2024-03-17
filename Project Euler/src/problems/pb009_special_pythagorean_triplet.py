def special_pythagorean_triplet(value_sum: int = 1000) -> dict:
    for a in range(500):
        for b in range(a + 1, 500):
            for c in range(b + 1, 500):
                if a + b + c == value_sum and is_pythagorean_triplet(a, b, c):
                    return {
                        "result": a * b * c,
                        "expected": 31875000,
                    }


def is_pythagorean_triplet(a: int, b: int, c: int) -> bool:
    return a < b < c and a**2 + b**2 == c**2
