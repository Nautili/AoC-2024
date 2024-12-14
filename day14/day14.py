import sys
import re
import operator
from functools import reduce


def simulate_robots(robots, steps, rows, cols):
    new_locs = []

    for robot in robots:
        row = (robot[0] + steps * robot[2]) % rows
        col = (robot[1] + steps * robot[3]) % cols
        new_locs.append((row, col))

    return new_locs


def get_quadrant_counts(robots):
    rows = max(robot[0] for robot in robots) + 1
    cols = max(robot[1] for robot in robots) + 1

    new_locs = simulate_robots(robots, 100, rows, cols)
    counts = [0] * 4
    for row, col in new_locs:
        if row != rows // 2 and col != cols // 2:
            quadrant = 2 * row // rows + 2 * (2 * col // cols)
            counts[quadrant] += 1

    return reduce(operator.mul, counts)


def get_easter_egg(robots):
    rows = max(robot[0] for robot in robots) + 1
    cols = max(robot[1] for robot in robots) + 1

    i = 0
    while True:
        locs = set(simulate_robots(robots, i, rows, cols))
        if len(locs) == len(robots):
            return i
        i += 1


def main():
    with open(sys.argv[1]) as f:
        lines = []
        for line in f.readlines():
            lines += [[int(val)
                       for val in re.sub("[^0-9-]", ' ', line).split()]]
    print(get_quadrant_counts(lines))
    print(get_easter_egg(lines))


if __name__ == '__main__':
    main()
