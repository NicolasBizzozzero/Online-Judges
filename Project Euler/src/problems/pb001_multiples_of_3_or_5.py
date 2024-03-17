def multiples_of_3_or_5(max_number: int = 1000) -> dict:
    result = 0
    for number in range(1, max_number):
        if is_divisible_by_3(number) or is_divisible_by_5(number):
            result += number
    return {
        "result": result,
        "expected": 233168,
    }


def is_divisible_by_3(number: int) -> bool:
    return number % 3 == 0


def is_divisible_by_5(number: int) -> bool:
    return number % 5 == 0
