import binascii
import base64
import string
import itertools
import codecs


LETTER_FREQUENCY = {
    # From http://www.data-compression.com/english.html
    "ENGLISH" : {
        'a': 0.0651738,
        'b': 0.0124248,
        'c': 0.0217339,
        'd': 0.0349835,
        'e': 0.1041442,
        'f': 0.0197881,
        'g': 0.0158610,
        'h': 0.0492888,
        'i': 0.0558094,
        'j': 0.0009033,
        'k': 0.0050529,
        'l': 0.0331490,
        'm': 0.0202124,
        'n': 0.0564513,
        'o': 0.0596302,
        'p': 0.0137645,
        'q': 0.0008606,
        'r': 0.0497563,
        's': 0.0515760,
        't': 0.0729357,
        'u': 0.0225134,
        'v': 0.0082903,
        'w': 0.0171272,
        'x': 0.0013692,
        'y': 0.0145984,
        'z': 0.0007836,
        ' ': 0.1918182 
    }
}

def iter_lines(filepath: str):
    """ Iterate lazily over the lines of a file. """
    with open(filepath) as file:
        for line in file:
            yield line.strip()


def bytes_to_string(bytes_to_convert: bytes) -> str:
    """ Return the string representation of bytes. """
    return str(bytes_to_convert)[2:-1]


def string_to_bytes(string_to_convert: str) -> bytes:
    """ Return a bytes array containing the string converted byte per byte. """
    return string_to_convert.encode("UTF8")


def encode_hex(hex_string: str) -> bytes:
    """ Convert hexadecimal string to bytes. """
    return codecs.decode(hex_string, "hex")


def decode_hex(hex_bytes: bytes) -> str:
    """ Convert bytes to hexadecimal string. """
    return codecs.encode(hex_bytes, "hex").decode()


def encode_base64(base64_string: str) -> bytes:
    """ Convert base64 string to bytes. """
    return bytes(base64_string, encoding="UTF8")


def decode_base64(base64_bytes: bytes) -> str:
    """ Convert bytes to a base64 string. """
    return base64_bytes.decode()


def hex_to_base64(hex_bytes: bytes) -> bytes:
    """ Convert hexadecimal bytes to base64 bytes. """
    return codecs.encode(hex_bytes, encoding="base64")[:-1]


def base64_to_hex(base64_bytes: bytes) -> bytes:
    """ Convert hexadecimal bytes to base64 bytes. """
    return codecs.decode(base64_bytes, encoding="base64")


def fixed_XOR(hex_bytes1: bytes, hex_bytes2: bytes) -> bytes:
    """ Compute the XOR combination of hex_bytes1 and hex_bytes2, two
    equal-length buffers.
    """
    if len(hex_bytes1) != len(hex_bytes2):
        raise ValueError("The two buffers need to be of equal-length")

    return bytes(x ^ y for (x, y) in zip(hex_bytes1, hex_bytes2))


def single_byte_XOR(hex_bytes: bytes, byte: bytes) -> bytes:
    """ Return hex_bytes XOR'd to a single byte. """
    byte = int(byte)
    return bytes(b ^ byte for b in hex_bytes)


def single_byte_XOR_cipher(hex_bytes: bytes) -> tuple:
    """ Decipher hex_bytes, a single-byte XOR'd hex encoded bytes using an
    english letter-frequency table.
    Return a tuple containing the key, the message and the score.
    """
    def score(bytes_message: bytes) -> int:
        score = 0
        for c in bytes_message:
            c = chr(c).lower()
            if c in LETTER_FREQUENCY["ENGLISH"]:
                score += LETTER_FREQUENCY["ENGLISH"][c]
        return score

    messages = [[c, single_byte_XOR(hex_bytes, c)] for c in range(256)]
    for message in messages:
        message.append(score(message[1]))

    key, message, score = max(messages, key=lambda p: p[2])

    return key, bytes_to_string(message), score


def repeating_key_XOR(hex_bytes: bytes, key: bytes) -> bytes:
    """ Return hex_bytes XOR'd to  repeating key. """
    return bytes(b ^ k for (b, k) in zip(hex_bytes, itertools.cycle(key)))


def hamming_distance(bytes1: bytes, bytes2: bytes) -> int:
    """ Compute the Hamming distance between two bytes.
    The Hamming distance is the number of differing bits between the two
    bytes.
    >>> hamming_distance(b"this is a test", b"wokka wokka!!!")
    37
    """
    return sum([bin(c1 ^ c2).count('1') for (c1, c2) in zip(bytes1, bytes2)])
