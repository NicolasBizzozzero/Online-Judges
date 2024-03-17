""" Finding the smallest number divisible by all numbers in [1, ..., 20] is the exact same as computing the Least
Common Multiple of all numbers between [1, ..., 20 ].

Links:
* https://en.wikipedia.org/wiki/Least_common_multiple

"""

from src.common.maths import lcm


def smallest_multiple(max_multiple: int = 20) -> dict:
    numbers = list(range(2, max_multiple + 1))
    return {
        "result": lcm(*numbers),
        "expected": 232792560,
    }
