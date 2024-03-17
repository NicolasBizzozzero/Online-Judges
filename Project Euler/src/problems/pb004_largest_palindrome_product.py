from src.common.maths import is_palindromic


def largest_palindrome_product(max_size: int = 1000) -> dict:
    max_palindrom = 0
    for product_a in range(max_size, 0, -1):
        for product_b in range(product_a, 0, -1):
            if is_palindromic((palindrom := product_a * product_b)):
                if palindrom > max_palindrom:
                    max_palindrom = palindrom
    return {
        "result": max_palindrom,
        "expected": 906609,
    }
