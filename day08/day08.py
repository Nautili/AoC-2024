import sys
from collections import defaultdict


def in_bounds(grid, loc):
    row, col = loc
    return row >= 0 and col >= 0 and row < len(grid) and col < len(grid[0])


def add(a, b):
    return tuple(a_val + b_val for a_val, b_val in zip(a, b))


def sub(a, b):
    return tuple(a_val - b_val for a_val, b_val in zip(a, b))


def mul(m, a):
    return tuple(m * a_val for a_val in a)


def add_single_antinode(left, right, grid, antinodes, k=1):
    delta = sub(left, right)
    added = False
    if in_bounds(grid, add(left, mul(k, delta))):
        antinodes.add(add(left, mul(k, delta)))
        added = True
    if in_bounds(grid, sub(right, mul(k, delta))):
        antinodes.add(sub(right, mul(k, delta)))
        added = True
    return added


def add_all_antinodes(left, right, grid, antinodes):
    k = 0
    while add_single_antinode(left, right, grid, antinodes, k):
        k += 1


def get_antinodes(grid, update_antinodes):
    antennae = defaultdict(list)
    for i, row in enumerate(grid):
        for j, val in enumerate(row):
            if val != '.':
                antennae[val] += [(i, j)]

    antinodes = set()
    for _, locs in antennae.items():
        for l in range(len(locs) - 1):
            for r in range(l + 1, len(locs)):
                update_antinodes(locs[l], locs[r], grid, antinodes)
    return antinodes


def main():
    with open(sys.argv[1]) as f:
        lines = [line.strip() for line in f.readlines()]
    print(len(get_antinodes(lines, add_single_antinode)))
    print(len(get_antinodes(lines, add_all_antinodes)))


if __name__ == '__main__':
    main()
