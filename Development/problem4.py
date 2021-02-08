import re

valid_eye_colors = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}


def check_fields_exists_part1(passport):
    # Part 2 has better implementation of this
    return all([k in passport for k in ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')])


def check_all_fields_exists(passport_fields):
    keys = passport_fields.keys()
    return all([key in keys for key in ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')])


def check_year(value, min_year, max_year):
    if re.match(r'(\d){4}', value) is None:
        return False

    return min_year <= int(value) <= max_year


def check_valid_hgt(value):
    height = re.match(r"(?P<height>\d*)(?P<type>cm|in)", value)

    if height is None:
        return False
    if height.group("type") == "cm" and 150 <= int(height.group("height")) <= 193:
        return True

    if height.group("type") == "in" and 59 <= int(height.group("height")) <= 76:
        return True

    return False


def check_valid_passport(passport):
    # Parse all key: value into a dict
    passport_fields = (dict([(field.split(':')[0], field.split(':')[1])
                             for field in re.findall(r'\w*:\S*', passport)]))

    if not check_all_fields_exists(passport_fields):
        return False

    # Check all fields are correct
    correct_patterns = {
        'byr': lambda field: check_year(field, 1920, 2002),
        'iyr': lambda field: check_year(field, 2010, 2020),
        'eyr': lambda field: check_year(field, 2020, 2030),
        'hgt': check_valid_hgt,
        'hcl': lambda field: re.match(r'#([0-9a-f]){6}', value) is not None,
        'ecl': lambda field: field in valid_eye_colors,
        'pid': lambda field: re.match(r'^[\d]{9}$', value) is not None,
        'cid': lambda _: True
    }

    for key, value in passport_fields.items():
        if not correct_patterns[key](value):
            return False

    return True


def problem4():
    with open(r"assets\p4_input.txt", 'r')as file_input:
        data = file_input.read()

        # Part 1:
        print(sum(1 for entry in data.split('\n\n') if check_fields_exists_part1(entry.strip())))

        # Part2:
        print(sum(1 for entry in data.split('\n\n') if check_valid_passport(entry.strip())))
