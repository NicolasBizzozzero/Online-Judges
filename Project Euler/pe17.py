

if __name__ == '__main__':
    units = ['one', 'two', 'three', 'four',
              'five', 'six', 'seven', 'eight',
              'nine', 'ten', 'eleven', 'twelve',
              'thirteen', 'fourteen', 'fifteen',
              'sixteen', 'seventeen', 'eighteen', 'nineteen']
    tens = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    others = ['hundred', 'thousand', 'and']
    
    char_count = 0
    for i in range(1, 1001):
        unit = i%10
        ten = (i//10)%10
        hundred = (i//100)%10
        thousand = (i//1000)%10

        if thousand != 0:
            char_count += len(units[0]) + len(others[1])
        if i%1000 != 0:
            if hundred != 0:
                char_count += len(units[hundred-1]) + len(others[0])
                if i%100 != 0:
                    char_count += len(others[2])
            if i%100 != 0:
                if ten < 2:
                    char_count += len(units[i%100-1])
                else:
                    char_count += len(tens[ten-2])
                    if unit != 0:
                        char_count += len(units[unit-1])
    print(char_count)