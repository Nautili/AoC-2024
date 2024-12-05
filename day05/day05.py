import sys
from collections import defaultdict


def get_valid_order(order, manual):
    seen = set()
    for i, val in enumerate(manual):
        seen.add(val)
        for next in order[val]:
            if next in seen:
                manual[manual.index(next)], manual[i] = \
                    manual[i], manual[manual.index(next)]
                get_valid_order(order, manual)
                return False  # signal this was initially out of order
    return True  # signal this was initially in order


def fix_valid(order, manuals):
    valid = 0
    invalid = 0
    for manual in manuals:
        if (get_valid_order(order, manual)):
            valid += manual[len(manual) // 2]
        else:
            invalid += manual[len(manual) // 2]
    return valid, invalid


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

        valid, invalid = fix_valid(order, manuals)
        print(valid)
        print(invalid)


if __name__ == '__main__':
    main()
