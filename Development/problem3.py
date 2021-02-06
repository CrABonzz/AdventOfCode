from functools import reduce
from typing import List


def count_slope_tree(grid: List[str], right_step: int, bottom_step: int) -> int:
    counter = 0
    row, col = 0, 0  # Start point

    while row < len(grid):
        if col >= len(grid[row]):
            col -= len(grid[row])

        if grid[row][col] == "#":
            counter += 1

        row += bottom_step
        col += right_step

    return counter


def slope_statistics(grid, *args):
    return [count_slope_tree(grid, right_step, bottom_step) for right_step, bottom_step in args]


def problem3():
    with open(r"assets\p3_input.txt", 'r')as file_input:
        grid = [line.strip() for line in file_input.readlines()]

        print(reduce(lambda x, y: x * y, slope_statistics(grid, (3, 1), (1, 1), (5, 1), (7, 1), (1, 2))))
