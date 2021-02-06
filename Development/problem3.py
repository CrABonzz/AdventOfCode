from functools import reduce
from typing import List


def count_slope_tree(grid: List[str], right_step: int, bottom_step: int, row: int, col: int) -> int:
    if row >= len(grid):
        return 0

    if col >= len(grid[row]):
        col -= len(grid[row])

    is_tree = 1 if grid[row][col] == "#" else 0

    return is_tree + count_slope_tree(grid, right_step, bottom_step, row+bottom_step, col+right_step)


def slope_statistics(grid, *args):
    # Start point 0, 0
    return [count_slope_tree(grid, right_step, bottom_step, 0, 0) for right_step, bottom_step in args]


def problem3():
    with open(r"assets\p3_input.txt", 'r')as file_input:
        grid = [line.strip() for line in file_input.readlines()]

        print(reduce(lambda x, y: x * y, slope_statistics(grid, (3, 1), (1, 1), (5, 1), (7, 1), (1, 2))))
