""" Cryptopals set 1 challenge 3.
## Single-byte XOR cipher
The hex encoded string:
1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736
... has been XOR'd against a single character. Find the key, decrypt the
message.
You can do this by hand. But don't: write code to do it for you.
How? Devise some method for "scoring" a piece of English plaintext.
Character frequency is a good metric. Evaluate each output and choose the one
with the best score.

### Achievement Unlocked
You now have our permission to make "ETAOIN SHRDLU" jokes on Twitter.

### Secret message
Cooking MC's like a pound of bacon
"""

from vrac import *


def str_single_byte_XOR_cipher(hex_string: str) -> tuple:
    return single_byte_XOR_cipher(encode_hex(hex_string))


def main():
    hex_string = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
    key, message, score = str_single_byte_XOR_cipher(hex_string)

    assert key == 88
    assert message == "Cooking MC's like a pound of bacon"


if __name__ == '__main__':
    main()
