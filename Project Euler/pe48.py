from math import pow

def main():
    sum = 0
    for i in range(1, 1001):
        sum += (i**i)
    print(sum%10000000000)

if __name__ == '__main__':
    main()