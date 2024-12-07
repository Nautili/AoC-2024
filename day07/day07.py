import sys


def is_reachable(target, curVal, values):
    if len(values) == 0:
        return curVal == target

    return is_reachable(target, curVal + values[0], values[1:]) or \
        is_reachable(target, curVal * values[0], values[1:])


def count_reachable(equations):
    return sum(equation[0] for equation in equations
               if is_reachable(equation[0], equation[1], equation[2:]))


def is_concat_reachable(target, curVal, values):
    if len(values) == 0:
        return curVal == target

    return is_concat_reachable(target, curVal + values[0], values[1:]) or \
        is_concat_reachable(target, curVal * values[0], values[1:]) or \
        is_concat_reachable(target, int(
            str(curVal) + str(values[0])), values[1:])


def count_concat_reachable(equations):
    return sum(equation[0] for equation in equations
               if is_concat_reachable(equation[0], equation[1], equation[2:]))


def main():
    with open(sys.argv[1]) as f:
        lines = [line.strip() for line in f.readlines()]
    equations = []
    for line in lines:
        equations += [[int(num.strip(':')) for num in line.split()]]
    print(count_reachable(equations))
    print(count_concat_reachable(equations))


if __name__ == '__main__':
    main()
