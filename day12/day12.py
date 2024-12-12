import sys
from collections import deque

DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def in_bounds(row, col, grid):
    return row >= 0 and row < len(grid) and col >= 0 and col < len(grid[0])


def get_area_price(row_s, col_s, grid, seen):
    area = 0
    perimeter = 0
    sides = 0

    frontier = deque()
    frontier.append((row_s, col_s))
    seen.add((row_s, col_s))

    while frontier:
        row, col = frontier.popleft()
        area += 1
        for d_row, d_col in DIRS:
            new_row = row + d_row
            new_col = col + d_col
            new_loc = (new_row, new_col)
            if in_bounds(new_row, new_col, grid) and \
               grid[new_row][new_col] == grid[row][col]:
                if new_loc not in seen:
                    frontier.append(new_loc)
                    seen.add(new_loc)
            else:
                perimeter += 1
                # wlog, assume that the perimeter is upwards. If the perimeter is the "leftmost"
                # part of the side, count it. This falls under two cases, with the perimeters marked
                # with a '~' as the part to count:
                #
                # 1. ...
                #    .+~
                #    .|o
                #
                # 2. x|.
                #    -+~
                #    .|o

                row_turn = row - d_col
                col_turn = col + d_row
                row_diag = row_turn + d_row
                col_diag = col_turn + d_col

                if not in_bounds(row_turn, col_turn, grid) or \
                        grid[row_turn][col_turn] != grid[row][col] or \
                        (in_bounds(row_diag, col_diag, grid) and
                            grid[row_diag][col_diag] == grid[row][col]):
                    sides += 1
    return area, perimeter, sides


def get_prices(grid):
    seen = set()
    area_total = 0
    side_total = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if (row, col) not in seen:
                area, perimeter, sides = get_area_price(row, col, grid, seen)
                area_total += area * perimeter
                side_total += area * sides
    return area_total, side_total


def main():
    with open(sys.argv[1]) as f:
        lines = [line.strip() for line in f.readlines()]
        area_total, side_total = get_prices(lines)
        print(area_total)
        print(side_total)


if __name__ == '__main__':
    main()
