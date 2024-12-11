import sys
from collections import defaultdict


def get_stone_count(stones, n):
    counts = defaultdict(int)
    for stone in stones:
        counts[stone] = 1

    for _ in range(n):
        new_counts = defaultdict(int)
        for stone, count in counts.items():
            if stone == 0:
                new_counts[1] += count
            elif len(s := str(stone)) % 2 == 0:
                new_counts[int(s[:len(s)//2])] += count
                new_counts[int(s[len(s)//2:])] += count
            else:
                new_counts[stone * 2024] += count
        counts = new_counts
    return sum(counts.values())


def main():
    with open(sys.argv[1]) as f:
        line = [int(val) for val in f.readline().strip().split()]
    print(get_stone_count(line, 25))
    print(get_stone_count(line, 75))


if __name__ == '__main__':
    main()
