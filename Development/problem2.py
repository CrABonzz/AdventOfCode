import re

def check_valid_line(line: str) -> bool:
    match = re.match(r'(?P<start>\d+)-(?P<end>[0-9]+) (?P<char>\D): (?P<password>\D+)', line)
    return int(match.group("start")) <= match.group('password').count(match.group('char')) <= int(match.group("end"))

def problem2():
    with open(r".\assets\p2_input.txt", 'r')as file_input:
        num_of_valid_pass = sum(1 for line in file_input.readlines() if check_valid_line(line))

        print(num_of_valid_pass)