from src.common.maths import is_even, fibonacci


def even_fibonacci_numbers(max_number: int = 4_000_000) -> dict:
    result = 0
    current_number = 0
    current_result = 0
    while current_result < max_number:
        if is_even(current_result):
            result += current_result
        current_result = fibonacci(current_number)
        current_number += 1
    return {
        "result": result,
        "expected": 4613732,
    }
