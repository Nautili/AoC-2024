import sys
from collections import deque

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def get_path(locs, steps):
    blocks = set(locs[:steps])
    rows = max(row for row, _ in locs) + 1
    cols = max(col for _, col in locs) + 1

    frontier = deque()
    frontier.append((0, 0, 0))
    seen = set()
    seen.add((0, 0))

    while frontier:
        row, col, dist = frontier.popleft()
        if (row, col) == (rows - 1, cols - 1):
            return dist
        for r_d, c_d in DIRS:
            new_row = row + r_d
            new_col = col + c_d
            new_loc = (new_row, new_col)
            if 0 <= new_row < rows and 0 <= new_col < cols and \
               new_loc not in seen and new_loc not in blocks:
                frontier.append((new_row, new_col, dist + 1))
                seen.add(new_loc)


def get_first_blockage(locs):
    lo = 0
    hi = len(locs) - 1

    while lo < hi:
        mid = (lo + hi) // 2
        if get_path(locs, mid):
            lo = mid + 1
        else:
            hi = mid - 1

    row, col = locs[lo]
    return f'{col},{row}'


def main():
    with open(sys.argv[1]) as f:
        lines = [line.strip().split(',') for line in f.readlines()]
        locs = [(int(row), int(col)) for col, row in lines]

        # print(get_path(locs, 12)) # example
        print(get_path(locs, 1024))  # actual
        print(get_first_blockage(locs))


if __name__ == '__main__':
    main()
