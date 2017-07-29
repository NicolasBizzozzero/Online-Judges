""" Cryptopals set 1 challenge 6.
## Break repeating-key XOR
It is officially on, now.
This challenge isn't conceptually hard, but it involves actual error-prone
coding. The other challenges in this set are there to bring you up to speed.
This one is there to qualify you. If you can do this one, you're probably just
fine up to Set 6.
There's a file here. It's been base64'd after being encrypted with
repeating-key XOR.
Decrypt it.
Here's how:
    Let KEYSIZE be the guessed length of the key; try values from 2 to (say)
    40. Write a function to compute the edit distance/Hamming distance between
    two strings. The Hamming distance is just the number of differing bits.
    The distance between:

    this is a test

    and

    wokka wokka!!!

    is 37. Make sure your code agrees before you proceed.
    For each KEYSIZE, take the first KEYSIZE worth of bytes, and the second
    KEYSIZE worth of bytes, and find the edit distance between them. Normalize
    this result by dividing by KEYSIZE.
    The KEYSIZE with the smallest normalized edit distance is probably the key.
    You could proceed perhaps with the smallest 2-3 KEYSIZE values. Or take 4
    KEYSIZE blocks instead of 2 and average the distances.
    Now that you probably know the KEYSIZE: break the ciphertext into blocks of
    KEYSIZE length.
    Now transpose the blocks: make a block that is the first byte of every
    block, and a block that is the second byte of every block, and so on.
    Solve each block as if it was single-character XOR. You already have code
    to do this.
    For each block, the single-byte XOR key that produces the best looking
    histogram is the repeating-key XOR key byte for that block. Put them
    together and you have the key.

This code is going to turn out to be surprisingly useful later on. Breaking
repeating-key XOR ("Vigenere") statistically is obviously an academic
exercise, a "Crypto 101" thing. But more people "know how" to break it than
can actually break it, and a similar technique breaks something much more
important.

### No, that's not a mistake.
We get more tech support questions for this challenge than any of the other
ones. We promise, there aren't any blatant errors in this text. In particular:
the "wokka wokka!!!" edit distance really is 37.
"""

import itertools
from vrac import *


def get_content_base64(filepath):
    return base64_to_hex(open(filepath, 'rb').read())


def is_odd(n: int) -> bool:
    return n % 2 == 1


def cut_in_half(sequence: slice, lefty: bool = True) -> tuple:
    """ Return a tuple containing sequence cut in half.
    If the sequence is of oddly length, the first half will contains one more
    element than the other half. This can be inversed with the lefty parameter
    (defaulting to True).
    """
    size = len(sequence)
    middle = size // 2
    if lefty and is_odd(size):
        middle += 1
    return sequence[:middle], sequence[middle:]


def chunker(iterable: iter, n: int, fillvalue=None) -> iter:
    """ Collect data into fixed-length chunks or blocks.
    >>> chunker('ABCDEFG', 3, 'x')
    ABC DEF Gxx
    """
    args = [iter(iterable)] * n
    return itertools.zip_longest(*args, fillvalue=fillvalue)


def take(n, iterable):
    "Return first n items of the iterable as a list"
    return list(itertools.islice(iterable, n))


def find_keysize(hex_bytes: bytes, max_keysize: int) -> int:
    """ For each KEYSIZE, take the first KEYSIZE worth of bytes, and the second
    KEYSIZE worth of bytes, and find the edit distance between them. Normalize
    this result by dividing by KEYSIZE.
    The KEYSIZE with the smallest normalized edit distance is probably the key.
    You could proceed perhaps with the smallest 2-3 KEYSIZE values. Or take 4
    KEYSIZE blocks instead of 2 and average the distances.
    """
    keysizes = dict()
    max_chunks = 3
    nb_chunks = 0

    for keysize in range(2, max_keysize + 1):
        for chunk in chunker(hex_bytes, keysize * 2):
            if nb_chunks > max_chunks:
                nb_chunks += 1
                chunk1, chunk2 = cut_in_half(chunk)
                print(chunk1, chunk2)
        nb_chunks = 0


def find_key_with_length(hex_bytes: bytes, key_length: int) -> bytes:
    blocks = [hex_bytes[i:i + key_length] for i in range(0, len(hex_bytes), key_length)]
    transposedBlocks = list(itertools.zip_longest(*blocks, fillvalue=0))
    key = [challenge3.breakSingleByteXOR(bytes(hex_bytes))[0] for hex_bytes in transposedBlocks]
    return bytes(key)


def break_repeating_key_XOR(filepath: str) -> str:
    hex_bytes = get_content_base64(filepath)
    keysize = find_keysize(hex_bytes, max_keysize=40)
    print("KEYSIZE:", keysize)

    return None, None


def main():
    filepath = "../res/6.txt"

    key, content = break_repeating_key_XOR(filepath)
    print(key, content)


if __name__ == '__main__':
    main()
