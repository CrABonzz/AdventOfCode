def part1(numbers):
    numbers.sort()
    numbers.insert(0, 0)    # The initial voltage

    differencess = [y - x for x, y in zip(numbers, numbers[1:])]

    # The 3 counts plus 1 for the main adapter
    return (differencess.count(3) + 1)*differencess.count(1)


def problem10():
    with open(r"assets\p10_input.txt", 'r')as file_input:
        numbers = [int(num) for num in file_input.readlines()]

    print("Part 1: ", part1(numbers))
