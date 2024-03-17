from typing import Iterable

from src.common.maths import is_prime
from itertools import islice


def batched(iterable: iter, n: int):
    """Batch data into tuples of length n. The last batch may be shorter.
    batched('ABCDEFG', 3) --> ABC DEF G
    """
    if n < 1:
        raise ValueError("n must be at least one")
    it = iter(iterable)
    while batch := tuple(islice(it, n)):
        yield batch


def cycle(iterable: iter):
    while True:
        for element in iterable:
            yield element


def rolling_window(iterable: iter, size: int):
    for i in range(len(iterable) - size + 1):
        yield iterable[i : i + size]


def iter_primes() -> int:
    """Infinite iterator through prime numbers."""
    yield 2

    i = 3
    while True:
        if is_prime(i):
            yield i
        i += 2


def chain(*iterators: Iterable) -> Iterable:
    for iterator in iterators:
        for element in iterator:
            yield element
