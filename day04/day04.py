import sys


def check_location(grid, row, col):
    hits = 0
    for row_diff in range(-1, 2):
        for col_diff in range(-1, 2):
            hits += all(grid[row + i * row_diff][col + i *
                        col_diff] == c for i, c in enumerate('XMAS'))
    return hits


def check_xmas(grid):
    total = 0
    for row in range(3, len(grid) - 3):
        for col in range(3, len(grid[row]) - 3):
            total += check_location(grid, row, col)
    return total


def get_middles(grid, row, col, middles):
    for row_diff in [-1, 1]:
        for col_diff in [-1, 1]:
            if all(grid[row + i * row_diff][col + i *
                                            col_diff] == c for i, c in enumerate('MAS')):
                new_a = (row + row_diff, col + col_diff)
                if new_a not in middles:
                    middles[new_a] = 0
                middles[new_a] += 1


def check_mas(grid):
    middles = {}
    for row in range(3, len(grid) - 3):
        for col in range(3, len(grid[row]) - 3):
            get_middles(grid, row, col, middles)
    return sum(v > 1 for _, v in middles.items())


def main():
    with open(sys.argv[1]) as f:
        lines = [line.strip() for line in f.readlines()]
        lines = ["###" + line + "###" for line in lines]
        lines = ["#" * len(lines[0])] * 3 + lines + ["#" * len(lines[0])] * 3
        print(check_xmas(lines))
        print(check_mas(lines))


if __name__ == '__main__':
    main()
