import sys
from collections import defaultdict


def check_location(grid, row, col):
    hits = 0
    for row_diff in range(-1, 2):
        for col_diff in range(-1, 2):
            hits += all(grid[row + i * row_diff]
                            [col + i * col_diff] == c for i, c in enumerate('XMAS'))
    return hits


def check_xmas(grid):
    total = 0
    for row in range(1, len(grid) - 1):
        for col in range(1, len(grid[row]) - 1):
            total += check_location(grid, row, col)
    return total


def get_middles(grid, row, col, middles):
    for row_diff in [-1, 1]:
        for col_diff in [-1, 1]:
            if all(grid[row + i * row_diff]
                       [col + i * col_diff] == c for i, c in enumerate('MAS')):
                middles[(row + row_diff, col + col_diff)] += 1


def check_mas(grid):
    middles = defaultdict(int)
    for row in range(1, len(grid) - 1):
        for col in range(1, len(grid[row]) - 1):
            get_middles(grid, row, col, middles)
    return sum(v > 1 for v in middles.values())


def main():
    with open(sys.argv[1]) as f:
        lines = [line.strip() for line in f.readlines()]
        lines = ["#" + line + "#" for line in lines]
        lines = ["#" * len(lines[0])] + lines + ["#" * len(lines[0])]
        print(check_xmas(lines))
        print(check_mas(lines))


if __name__ == '__main__':
    main()
