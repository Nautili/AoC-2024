import sys
from queue import PriorityQueue

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def solve_maze(grid):
    pending = PriorityQueue()
    # val, row, col, dir
    pending.put((0, len(grid) - 2, 1, 0))
    seen = set()

    while pending:
        val, row, col, dir = pending.get()
        if (row, col, dir) in seen:
            continue
        seen.add((row, col, dir))

        if (row, col) == (1, len(grid[0]) - 2):
            return val

        d_row, d_col = DIRS[dir]
        if grid[row + d_row][col + d_col] != '#':
            pending.put((val + 1, row + d_row, col + d_col, dir))
        pending.put((val + 1000, row, col, (dir - 1) % 4))
        pending.put((val + 1000, row, col, (dir + 1) % 4))


def get_paths(grid):
    pending = PriorityQueue()
    # val, row, col, dir, path
    pending.put((0, len(grid) - 2, 1, 0, [(len(grid) - 2, 1)]))
    seen = {}

    while pending:
        val, row, col, dir, path = pending.get()
        if (row, col, dir) in seen and seen[(row, col, dir)] < val:
            continue
        seen[(row, col, dir)] = val

        if (row, col) == (1, len(grid[0]) - 2):
            locs = set(path)
            while pending:
                new_val, _, _, _, path = pending.get()
                if new_val > val:
                    return len(locs)
                locs.update(path)

        d_row, d_col = DIRS[dir]
        new_row = row + d_row
        new_col = col + d_col
        if grid[new_row][new_col] != '#':
            pending.put((val + 1, new_row, new_col,
                        dir, path + [(new_row, new_col)]))
        pending.put((val + 1000, row, col, (dir - 1) % 4, path))
        pending.put((val + 1000, row, col, (dir + 1) % 4, path))


def main():
    with open(sys.argv[1]) as f:
        grid = [list(line.strip()) for line in f.readlines()]

    print(solve_maze(grid))
    print(get_paths(grid))


if __name__ == '__main__':
    main()
