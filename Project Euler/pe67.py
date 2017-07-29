def get_line(filepath: str, line_index: int) -> str:
    current_index = 1
    with open(filepath) as file:
        for line in file:
            if current_index == line_index:
                return line
            current_index += 1
    return ""


def get_number_of_lines(filepath: str) -> int:
    lines = 0
    with open(filepath) as file:
        for line in file:
            lines += 1
    return lines


def get_lines(filepath: str, floor: int, ceil: int) -> str:
    content = ""
    current_line = 1
    with open(filepath) as file:
        for line in file:
            if current_line >= ceil:
                break
            if current_line >= floor:
                content += line
            current_line += 1
    return content


def get_content(filepath: str) -> str:
    content = ""
    with open(filepath) as file:
        for line in file:
            content += line
    return content


def delete_last_line(filepath: str) -> None:
    content = get_lines(filepath, 0, get_number_of_lines(filepath) - 1)
    create_file(filepath, content)


def create_file(filepath: str, content=""):
    with open(filepath, 'w') as file:
        file.write(content)


def append_line(filepath: str, line: str) -> None:
    with open(filepath, 'a') as file:
        file.write(line)


def compute_newline(upper_line: str, lower_line: str) -> str:
    up_numbers = upper_line.split()
    lo_numbers = lower_line.split()
    arrstr_to_arrint(up_numbers)
    arrstr_to_arrint(lo_numbers)
    for i in range(len(lo_numbers) - 1):
        up_numbers[i] += max(lo_numbers[i], lo_numbers[i + 1])
    # Construct string to return
    str_to_return = ""
    for n in up_numbers:
        str_to_return += str(n) + ' '
    return str_to_return[:-1]


def arrstr_to_arrint(arrstr: list) -> list:
    for i in range(len(arrstr)):
        arrstr[i] = int(arrstr[i])


def print_file(filepath: str):
    with open(filepath) as file:
        for line in file:
            print(line)


if __name__ == "__main__":
    file = r"../res/67_triangle.txt"
    content = get_content(file)
    nb_of_lines = get_number_of_lines(file)
    while nb_of_lines > 1:
        lower_line = get_line(file, nb_of_lines)
        upper_line = get_line(file, nb_of_lines - 1)
        newline = compute_newline(upper_line, lower_line)
        delete_last_line(file)
        append_line(file, newline)
        nb_of_lines -= 1
    print_file(file)
    create_file(file, content)
