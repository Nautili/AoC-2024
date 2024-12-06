import sys


def find_start(grid):
    for row, grid_row in enumerate(grid):
        for col, val in enumerate(grid_row):
            if val == '^':
                return (row, col)


def get_traveled_path(grid):
    row, col = find_start(grid)
    row_d = -1
    col_d = 0
    seen = set()
    while row + row_d >= 0 and row + row_d < len(grid) and \
            col + col_d >= 0 and col + col_d < len(grid[0]):
        if (row, col, row_d, col_d) in seen:
            return set((row, col) for row, col, _, _ in seen), True
        seen.add((row, col, row_d, col_d))
        while grid[row + row_d][col + col_d] == '#':
            row_d, col_d = col_d, -row_d  # rotate
        row += row_d
        col += col_d
    seen.add((row, col, row_d, col_d))
    return set((row, col) for row, col, _, _ in seen), False


def count_possible_loops(grid):
    total = 0
    traveled = get_traveled_path(grid)[0]
    for row, col in traveled:
        if grid[row][col] == '.':  # avoid the start
            grid[row][col] = '#'
            total += get_traveled_path(grid)[1]
            grid[row][col] = '.'
    return total


def main():
    with open(sys.argv[1]) as f:
        lines = [list(line.strip()) for line in f.readlines()]
        print(len(get_traveled_path(lines)[0]))
        print(count_possible_loops(lines))


if __name__ == '__main__':
    main()
