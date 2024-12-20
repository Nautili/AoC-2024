import sys
from collections import defaultdict, deque

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def get_start(grid):
    for i, line in enumerate(grid):
        for j, val in enumerate(line):
            if val == 'S':
                return (i, j)


def get_default_path(grid, row, col):
    dists = defaultdict(int)
    pending = deque()
    pending.append((row, col))
    seen = set()
    seen.add((row, col))
    path_len = sum(1 for row in grid for val in row if val != '#')

    while pending:
        row, col = pending.popleft()
        path_len -= 1
        dists[(row, col)] = path_len

        for d_r, d_c in DIRS:
            new_row = row + d_r
            new_col = col + d_c
            if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and \
                    (new_row, new_col) not in seen and grid[new_row][new_col] != '#':
                pending.append((new_row, new_col))
                seen.add((new_row, new_col))
    return dists


def get_faster_paths(grid, thresh, skips):
    row, col = get_start(grid)
    default_path = get_default_path(grid, row, col)
    counts = defaultdict(int)

    for ((s_row, s_col), s_len) in default_path.items():
        for row in range(max(0, s_row - skips), min(len(grid), s_row + skips + 1)):
            for col in range(max(0, s_col - skips), min(len(grid[0]), s_col + skips + 1)):
                dist = abs(s_row - row) + abs(s_col - col)
                if dist <= skips and grid[row][col] != '#':
                    counts[s_len - dist - default_path[(row, col)]] += 1

    return sum(count for saved, count in counts.items() if saved >= thresh)


def main():
    with open(sys.argv[1]) as f:
        grid = [line.strip() for line in f.readlines()]

    print(get_faster_paths(grid, thresh=100, skips=2))
    print(get_faster_paths(grid, thresh=100, skips=20))


if __name__ == '__main__':
    main()
