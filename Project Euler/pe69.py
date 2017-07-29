

def euleurs_totient(n: int) -> int:
    pass


def main():
    max = 0
    for i in range(2, 1000001):
        totient = i / euleurs_totient(i)
        if totient > max:
            max = totient
    print(max)


if __name__ == "__main__":
    main()