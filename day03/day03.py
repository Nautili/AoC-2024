import sys
import re


def get_muls(line):
    p = re.compile(r"mul\((\d+),(\d+)\)")
    return sum(int(a) * int(b) for a, b in p.findall(line))


def get_enabled_muls(line):
    line = re.sub(r"don't\(\).*?do\(\)", "", line)
    return get_muls(line)


def main():
    with open(sys.argv[1]) as f:
        line = ''.join(line.strip() for line in f.readlines())
        print(get_muls(line))
        print(get_enabled_muls(line))


if __name__ == '__main__':
    main()
