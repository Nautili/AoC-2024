import sys
from time import sleep

DIRS = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}


def find_robot(grid):
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == '@':
                return (row, col)


def simulate_moves(grid, moves):
    row, col = find_robot(grid)

    for move in moves:
        d_row, d_col = DIRS[move]
        steps = 1
        while (val := grid[row + steps * d_row][col + steps * d_col]) not in '.#':
            steps += 1
        if val == '.':
            grid[row + steps * d_row][col + steps * d_col] = 'O'
            grid[row + d_row][col + d_col] = '@'
            grid[row][col] = '.'
            row += d_row
            col += d_col


def swap(grid, row, col, new_row, new_col):
    grid[row][col], grid[new_row][new_col] = grid[new_row][new_col], grid[row][col]


def push(grid, move, row, col, do_swap=False):
    if grid[row][col] == '#':
        return False
    if grid[row][col] == '.':
        return True

    d_row, d_col = DIRS[move]
    new_row = row + d_row
    new_col = col + d_col

    will_move = push(grid, move, new_row, new_col, do_swap)
    if will_move and move in '^v':
        if grid[row][col] == '[':
            grid[row][col] = '{'
            if grid[row][col + 1] == ']':
                will_move = push(grid, move, row, col + 1, do_swap)
            grid[row][col] = '['
        elif grid[row][col] == ']':
            grid[row][col] = '}'
            if grid[row][col - 1] == '[':
                will_move = push(grid, move, row, col - 1, do_swap)
            grid[row][col] = ']'
    if do_swap:
        swap(grid, row, col, new_row, new_col)
    return will_move


def simulate_wide_moves(grid, moves):
    for move in moves:
        row, col = find_robot(grid)
        if push(grid, move, row, col, do_swap=False):
            push(grid, move, row, col, do_swap=True)

    # print(move)
    # for line in grid:
    #     print(''.join(line))


def box_count(grid):
    count = 0
    for row, line in enumerate(grid):
        for col, val in enumerate(line):
            if val in '[O':
                count += 100 * row + col
    return count


def widen_grid(grid):
    wide_grid = []
    for row in grid:
        line = []
        for val in row:
            if val == '#':
                line += ['#', '#']
            elif val == 'O':
                line += ['[', ']']
            elif val == '.':
                line += ['.', '.']
            elif val == '@':
                line += ['@', '.']
        wide_grid += [line]
    return wide_grid


def main():
    grid = []
    moves = []
    with open(sys.argv[1]) as f:
        for line in f.readlines():
            if '#' in line:
                grid += [list(line.strip())]
            elif line[0] in '<^>v':
                moves += list(line.strip())
    wide_grid = widen_grid(grid)

    simulate_moves(grid, moves)
    print(box_count(grid))
    simulate_wide_moves(wide_grid, moves)
    print(box_count(wide_grid))


if __name__ == '__main__':
    main()
