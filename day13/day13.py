import sys
import re


def get_button_pushes(problem):
    button_a, button_b, prize = problem
    a_x, a_y = button_a
    b_x, b_y = button_b
    p_x, p_y = prize

    det = a_x * b_y - a_y * b_x
    adj_a = (p_x * b_y - b_x * p_y)
    adj_b = (a_x * p_y - p_x * a_y)
    # check for no solution and non-integer solutions
    if det == 0 or adj_a % det != 0 or adj_b % det != 0:
        return 0

    return (adj_a * 3 + adj_b) // det


def get_all_button_pushes(problems):
    return sum(get_button_pushes(problem) for problem in problems)


def get_large_button_pushes(problems):
    for problem in problems:
        problem[2] = [val + 10000000000000 for val in problem[2]]
    return sum(get_button_pushes(problem) for problem in problems)


def main():
    problems = []
    with open(sys.argv[1]) as f:
        raw = f.readlines()
    raw = [raw[i:i+3] for i in range(0, len(raw), 4)]
    for group in raw:
        problem = []
        for line in group:
            problem += [[int(val)
                        for val in re.sub('[^0-9 ]', '', line).split()]]
        problems += [problem]
    print(get_all_button_pushes(problems))
    print(get_large_button_pushes(problems))


if __name__ == '__main__':
    main()
