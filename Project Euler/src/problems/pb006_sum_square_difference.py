def sum_square_difference(max_number: int = 100) -> dict:
    return {
        "result": square_of_sum(max_number=max_number)
        - sum_of_square(max_number=max_number),
        "expected": 25164150,
    }


def sum_of_square(max_number: int) -> int:
    result = 0
    for i in range(1, max_number + 1):
        result += i**2
    return result


def square_of_sum(max_number: int) -> int:
    """Thanks to Euler's formula, equals to (n \ times (n + 1)) / 2"""
    sum_of_numbers = (max_number * (max_number + 1)) / 2
    return int(sum_of_numbers**2)
