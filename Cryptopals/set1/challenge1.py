""" Cryptopals set 1 challenge 1.
## Convert hex to base64
The string:
49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d
Should produce:
SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t
So go ahead and make that happen. You'll need to use this code for the rest of
the exercises. 

### Cryptopals Rule
Always operate on raw bytes, never on encoded strings.
Only use hex and base64 for pretty-printing.

### Secret message
I'm killing your brain like a poisonous mushroom
"""

from vrac import *


def str_hex_to_base64(hex_string: str) -> str:
    """ Convert hexadecimal string to base64. """
    return decode_base64(hex_to_base64(encode_hex(hex_string)))


def str_base64_to_hex(base64_string: str) -> str:
    """ Convert base64 string to hexadecimal. """
    return decode_hex(base64_to_hex(encode_base64(base64_string)))


def main():
    # hex to base64
    hex_string = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
    base64_string = str_hex_to_base64(hex_string)
    assert base64_string == "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"

    # base64 to hex
    hex_string = str_base64_to_hex(base64_string)
    assert hex_string == "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"


if __name__ == '__main__':
    main()
