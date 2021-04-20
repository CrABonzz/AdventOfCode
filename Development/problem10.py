def part2(numbers):
    ways = {numbers[-1]: 1}     # The final step

    for number in reversed(numbers[:-1]):
        ways[number] = sum(ways[number + next_diff] for next_diff in range(1, 4) if number + next_diff in numbers)

    return ways[0]


def problem10():
    with open(r"assets\p10_input.txt", 'r')as file_input:
        numbers = [int(num) for num in file_input.readlines()]

    # Add initial and final voltages
    numbers.sort()
    numbers.insert(0, 0)
    numbers.append(max(numbers) + 3)

    differences = [y - x for x, y in zip(numbers, numbers[1:])]

    part1 = "1-jolt multiplied by 3-jolt differences:" + str(differences.count(3) * differences.count(1))
    print("The number of ways: ", part2(numbers))
