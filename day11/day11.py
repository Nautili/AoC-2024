import sys
from functools import cache


@cache
def get_stone_count(stone, count):
    if count == 0:
        return 1

    if stone == 0:
        return get_stone_count(1, count - 1)
    elif len(s := str(stone)) % 2 == 0:
        return get_stone_count(int(s[:len(s)//2]), count - 1) + \
            get_stone_count(int(s[len(s)//2:]), count - 1)
    else:
        return get_stone_count(stone * 2024, count - 1)


def get_stones(line, count):
    return sum(get_stone_count(stone, count) for stone in line)


def main():
    with open(sys.argv[1]) as f:
        line = [int(val) for val in f.readline().strip().split()]
    print(get_stones(line, 25))
    print(get_stones(line, 75))


if __name__ == '__main__':
    main()
