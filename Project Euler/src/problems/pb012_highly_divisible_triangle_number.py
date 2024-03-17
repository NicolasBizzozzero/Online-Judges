from src.common.maths import divisors_of, triangle_number


def highly_divisible_triangle_number() -> dict:
    idx_triangle_number = 1
    while len(divisors_of(triangle_number(idx_triangle_number))) < 500:
        idx_triangle_number += 1

    return {
        "result": triangle_number(idx_triangle_number),
        "expected": 76576500,
    }
