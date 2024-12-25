import sys


def get_counts(block):
    counts = []
    for col in range(len(block[0])):
        cur_count = 0
        for row in range(len(block)):
            if block[row][col] == '#':
                cur_count += 1
        counts += [cur_count]
    return counts


def get_valid_combos(keys, locks):
    return sum(all(l + r < 8 for l, r in zip(key, lock)) for key in keys for lock in locks)


def main():
    with open(sys.argv[1]) as f:
        lines = [line.strip() for line in f.readlines()]

    raw_blocks = [lines[i:i+7] for i in range(0, len(lines), 8)]
    keys = []
    locks = []
    for block in raw_blocks:
        if block[0][0] == '#':
            locks += [block]
        else:
            keys += [block]

    keys = [get_counts(key) for key in keys]
    locks = [get_counts(lock) for lock in locks]
    print(get_valid_combos(keys, locks))


if __name__ == '__main__':
    main()
