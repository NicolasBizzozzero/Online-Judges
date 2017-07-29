""" Cryptopals set 1 challenge 4.
## Detect single-character XOR
One of the 60-character strings in this file has been encrypted by
single-character XOR.
Find it.
(Your code from #3 should help.)

### Secret message
Now that the party is jumping

"""

from vrac import *


def detect_single_character_XOR(filepath: str) -> tuple:
    """ Find the encrypted message with a single-character XOR stored in
    filepath. Return a tuple containing the single character and the message.
    """
    encoded_lines = (single_byte_XOR_cipher(encode_hex(line)) for line in iter_lines(filepath))
    return max(encoded_lines, key=lambda p: p[2])


def main():
    filepath = "../res/4.txt"
    key, message, score = detect_single_character_XOR(filepath)

    assert key == 53
    assert message == r"Now that the party is jumping\n"


if __name__ == '__main__':
    main()
