import sys
from collections import Counter


def main():
    with open(sys.argv[1]) as f:
        lines = [[int(val) for val in line.split()] for line in f.readlines()]
        # part 1
        first_line, second_line = zip(*lines)
        print(sum(abs(a - b)
              for a, b in zip(sorted(first_line), sorted(second_line))))

        # part 2
        counts = Counter(second_line)
        print(sum(a * counts[a] for a in first_line))


if __name__ == '__main__':
    main()
