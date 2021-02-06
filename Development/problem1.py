from typing import List


def sumTwo(values: List[int], target: int) -> tuple[int, int]:
    seen_values = set()

    for val in values:
        if target - val in seen_values:
            return val, target-val
        seen_values.add(val)


def problem1():
    with open(r"C:\Users\User\Desktop\mega\edu\Projects\AoC\AdventOfCode\Development\assets\p1_input.txt", 'r')as file_input:
        file_data = file_input.read()
        values = [int(val) for val in file_data.strip().split("\n")]
        val1, val2 = sumTwo(values, 2020)
        print(val1*val2)
