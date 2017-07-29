def is_pandigital(n):
    if not (0 < n < 1000000000):
        return False
    n = str(n)
    digits = [str(i) for i in range(1, len(n)+1)]
    for digit in digits:
        if digit in n:
            n = n.replace(digit, "")
        else:
            return False
    # Maybe a n containing the digit 0 can cause issues
    if len(n) == 0:
        return True
    return False

if __name__ == '__main__':
    pass

