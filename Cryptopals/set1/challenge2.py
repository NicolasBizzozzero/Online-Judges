""" Cryptopals set 1 challenge 2.
## Fixed XOR
Write a function that takes two equal-length buffers and produces their XOR
combination.
If your function works properly, then when you feed it the string:
1c0111001f010100061a024b53535009181c
... after hex decoding, and when XOR'd against:
686974207468652062756c6c277320657965
... should produce:
746865206b696420646f6e277420706c6179

### Secrets messages
hit the bull's eye
the kid don't play
"""

from vrac import *


def str_fixed_XOR(hex_string1: str, hex_string2: str) -> str:
    hex_bytes1 = encode_hex(hex_string1)
    hex_bytes2 = encode_hex(hex_string2)
    xored_bytes = fixed_XOR(hex_bytes1, hex_bytes2)
    return decode_hex(xored_bytes)


def main():
    hex_string1 = "1c0111001f010100061a024b53535009181c"
    hex_string2 = "686974207468652062756c6c277320657965"
    xored_string = str_fixed_XOR(hex_string1, hex_string2)

    assert xored_string == "746865206b696420646f6e277420706c6179"


if __name__ == '__main__':
    main()
