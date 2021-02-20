PREMABLE_LENGTH = 25


def sum_two(numbers, target):
    seen_values = set()

    for val in numbers:
        if target - val in seen_values:
            return True
        seen_values.add(val)

    return False


def find_not_valid(all_numbers, premable_length):
    numbers = set(all_numbers[:premable_length])

    for number in all_numbers[25:]:
        if not sum_two(numbers, number):
            return number

        numbers.add(number)


def find_contiguious_set(numbers, target_value):
    set_length = 2

    while True:
        for index, _ in enumerate(numbers):
            if target_value == sum(numbers[index: index + set_length]):
                contiguous_numbers = numbers[index: index + set_length]
                return min(contiguous_numbers) + max(contiguous_numbers)

        set_length += 1


def problem9():
    with open(r"assets\p9_input.txt", 'r')as file_input:
        numbers = file_input.readlines()

    numbers = [int(number) for number in numbers]
    non_valid = find_not_valid(numbers, PREMABLE_LENGTH)
    print("Part 1: First non-valid number", non_valid)

    set_sum = find_contiguious_set(numbers, non_valid)
    print("Part 2: contiguous set sums to", set_sum)
