import sys

def is_good_report(line):
    diffs = [a - b for a, b in zip(line[:-1], line[1:])]
    return all(0 < diff < 4 for diff in diffs) or all(-4 < diff < 0 for diff in diffs)

def is_good_report_except_one(line):
    for i in range(len(line)):
        new_line = line[:i] + line[i + 1:]
        diffs = [a - b for a, b in zip(new_line[:-1], new_line[1:])]
        if all(0 < diff < 4 for diff in diffs) or all(-4 < diff < 0 for diff in diffs):
            return True
    return False

def main():
    with open(sys.argv[1]) as f:
        lines = [[int(val) for val in line.split()] for line in f.readlines()]
        print(sum(is_good_report(line) for line in lines))
        print(sum(is_good_report_except_one(line) for line in lines))


if __name__ == '__main__':
    main()
