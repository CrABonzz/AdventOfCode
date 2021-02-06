from functools import reduce
from typing import List


def sumTwo(values: List[int], target: int) -> tuple[int, int]:
    seen_values = set()

    for val in values:
        if target - val in seen_values:
            return val, target - val
        seen_values.add(val)

    raise ValueError("Not found")


def sumThree(values: List[int], target: int) -> tuple[int, int, int]:
    for val in values:
        values.remove(val)

        try:
            val1, val2 = sumTwo(values, target - val)
            return val, val1, val2
        except ValueError:
            values.append(val)


def problem1():
    with open(r".\assets\p1_input.txt", 'r')as file_input:
        file_data = file_input.read()
        values = [int(val) for val in file_data.strip().split("\n")]

        part1 = reduce(lambda x, y: (x * y), sumTwo(values, 2020))

        part2 = reduce(lambda x, y: (x * y), sumThree(values, 2020))

        print(part1, part2)
