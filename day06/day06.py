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
        seen.add((row, col))
        while grid[row + row_d][col + col_d] == '#':
            row_d, col_d = col_d, -row_d  # rotate
        row += row_d
        col += col_d
    # +1 here to count the last edge. There only way to reach the edge is when
    # leaving, so this should be safe
    return len(seen) + 1


def path_has_loop(grid):
    row, col = find_start(grid)
    row_d = -1
    col_d = 0
    seen = set()
    while row + row_d >= 0 and row + row_d < len(grid) and \
            col + col_d >= 0 and col + col_d < len(grid[0]):
        if (row, col, row_d, col_d) in seen:
            return True
        seen.add((row, col, row_d, col_d))
        while grid[row + row_d][col + col_d] == '#':
            row_d, col_d = col_d, -row_d  # rotate
        row += row_d
        col += col_d
    return False


def count_possible_loops(grid):
    total = 0
    for row, grid_row in enumerate(grid):
        for col, val in enumerate(grid_row):
            if val == '.':
                grid[row][col] = '#'
                total += path_has_loop(grid)
                grid[row][col] = '.'
    return total


def main():
    with open(sys.argv[1]) as f:
        lines = [list(line.strip()) for line in f.readlines()]
        print(get_traveled_path(lines))
        print(count_possible_loops(lines))


if __name__ == '__main__':
    main()
