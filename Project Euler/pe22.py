def parse_file_into_list(file):
    lst = [] 
    with open(file, "r") as f:
        for line in f:
            line = line.replace("\"", "")
            line = line.replace(",", " ")
            lst = line.split()
    return lst


def name_score(name):
    score = 0
    for char in name:
        score += ord(char)-64
    return score

if __name__ == "__main__":
    lstOfNames = parse_file_into_list("names.txt")
    lstOfNames.sort()
    sum = 0
    position = 1
    for name in lstOfNames:
        sum += (position * name_score(name))
        position += 1
    print(sum)
    