import sys
from collections import defaultdict


def is_valid(order, manual):
    seen = set()
    for val in manual:
        seen.add(val)
        for next in order[val]:
            if next in seen:
                return False
    return True


def count_valid(order, manuals):
    valid = 0
    for manual in manuals:
        if (is_valid(order, manual)):
            valid += manual[len(manual) // 2]
    return valid


def get_valid_order(order, manual):
    seen = set()
    for i, val in enumerate(manual):
        seen.add(val)
        for next in order[val]:
            if next in seen:
                manual[manual.index(next)], manual[i] = \
                    manual[i], manual[manual.index(next)]
                get_valid_order(order, manual)
                return


def fix_valid(order, manuals):
    valid = 0
    for manual in manuals:
        if (not is_valid(order, manual)):
            get_valid_order(order, manual)
            valid += manual[len(manual) // 2]
    return valid


def main():
    with open(sys.argv[1]) as f:
        lines = [line.strip() for line in f.readlines()]
        order = defaultdict(list)
        manuals = []
        for line in lines:
            if '|' in line:
                before, after = line.split('|')
                order[int(before)] += [int(after)]
            elif ',' in line:
                manuals += [[int(val) for val in line.split(',')]]
        print(count_valid(order, manuals))
        print(fix_valid(order, manuals))


if __name__ == '__main__':
    main()
