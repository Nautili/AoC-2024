import sys
from collections import defaultdict, deque

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def get_rating(grid, loc):
    counts = defaultdict(int)
    counts[loc] = 1
    pending = deque()
    pending.append(loc)
    rating = 0
    score = 0

    while pending:
        row, col = pending.popleft()
        if grid[row][col] == 9:
            rating += counts[(row, col)]
            score += 1
            continue

        for d_row, d_col in DIRS:
            new_row = row + d_row
            new_col = col + d_col
            new_loc = (new_row, new_col)
            if new_row >= 0 and new_row < len(grid) and \
               new_col >= 0 and new_col < len(grid[0]) and \
               grid[row][col] + 1 == grid[new_row][new_col]:
                if new_loc not in counts:
                    pending.append(new_loc)
                counts[new_loc] += counts[(row, col)]
    return score, rating


def get_ratings(grid):
    score = 0
    rating = 0
    for i, row in enumerate(grid):
        for j, val in enumerate(row):
            if val == 0:
                cur_score, cur_rating = get_rating(grid, (i, j))
                score += cur_score
                rating += cur_rating
    return score, rating


def main():
    with open(sys.argv[1]) as f:
        grid = [[int(val) for val in line.strip()] for line in f.readlines()]
        score, rating = get_ratings(grid)
        print(score)
        print(rating)


if __name__ == '__main__':
    main()
