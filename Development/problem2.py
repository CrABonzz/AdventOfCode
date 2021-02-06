import re

def break_line(line: str):
    match = re.match(r'(?P<start>\d+)-(?P<end>[0-9]+) (?P<char>\D): (?P<password>\D+)', line)
    return int(match.group("start")), int(match.group("end")), match.group("char"), match.group("password")


def check_valid_line_part1(line: str) -> bool:
    start, end, character, password = break_line(line)
    return start <= password.count(character) <= end


def check_valid_line_part2(line: str) -> bool:
    start, end, character, password = break_line(line)
    return (password[start-1] == character) ^ (password[end-1] == character)



def problem2():
    with open(r".\assets\p2_input.txt", 'r')as file_input:
        lines = file_input.readlines()
        valid_lines_part1 = sum(1 for line in lines if check_valid_line_part1(line))

        valid_lines_part2 = sum(1 for line in lines if check_valid_line_part2(line))

        print(valid_lines_part1, valid_lines_part2)