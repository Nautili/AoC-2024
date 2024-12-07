import sys


def is_reachable(target, curVal, values, check_concat=False):
    if (curVal > target):
        return False

    if len(values) == 0:
        return curVal == target

    return is_reachable(target, curVal + values[0], values[1:], check_concat) or \
        is_reachable(target, curVal * values[0], values[1:], check_concat) or \
        (check_concat and is_reachable(target,
                                       int(str(curVal) + str(values[0])),
                                       values[1:],
                                       check_concat))


def count_reachable(equations, check_concat=False):
    return sum(equation[0] for equation in equations
               if is_reachable(equation[0], equation[1], equation[2:], check_concat))


def main():
    with open(sys.argv[1]) as f:
        lines = [line.strip() for line in f.readlines()]
    equations = [[int(num.strip(':')) for num in line.split()]
                 for line in lines]
    print(count_reachable(equations))
    print(count_reachable(equations, check_concat=True))


if __name__ == '__main__':
    main()
