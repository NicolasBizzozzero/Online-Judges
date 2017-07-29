dic_char_to_ap = {}


def get_triangular_number(n: int) -> int:
    """Return the value of the nth triangular number.
        A triangular number n is the sum of all integers inferior
        or equal to n.
    """
    return (n * (n + 1)) / 2


def is_triangular_number(n: int) -> bool:
    """Return True if n is a triangular number, False otherwise. """
    return is_perfect_square((8 * n) + 1)


def is_perfect_square(n: int) -> bool:
    """Return True if n is a perfect square, False otherwise.
        A perfect square is a number who has for square root
        another integer.
        This function use the Babylonian method to compute its
        result.
    """
    x = n // 2
    seen = set([x])
    while x * x != n:
        x = (x + (n // x)) // 2
        if x in seen:
            return False
        seen.add(x)
    return True


def alphabetical_position(char: str) -> int:
    """Return the alphabetical position a char. """
    return ord(char.upper()) - 64


def is_triangular_word(word: str) -> bool:
    """Return True if word is a triangular word.
        A triangular word is a word who the sum of
        all the alphabetical position of its characters
        is equals to a triangular number.
    """
    sum_of_char = 0
    for char in word:
        sum_of_char += dic_char_to_ap[char]
    return is_triangular_number(sum_of_char)


def get_list_of_words_from_file(file: str) -> list:
    with open(file, 'r') as f:
        list_of_words = f.readlines()
    list_of_words = list_of_words[0].split(",")
    for i in range(len(list_of_words)):
        list_of_words[i] = list_of_words[i].strip("\"")
    return list_of_words


def main():
    counter = 0
    list_of_words = get_list_of_words_from_file("words.txt")
    for word in list_of_words:
        if is_triangular_word(word):
            counter += 1
    print(counter)


if __name__ == "__main__":
    dic_char_to_ap = {c: alphabetical_position(
        c) for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"}
    main()
