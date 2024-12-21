import sys
from functools import cache


DIR_PAD = {
    'l': (0, 0),
    'd': (0, 1),
    'r': (0, 2),
    'X': (1, 0),
    'u': (1, 1),
    'A': (1, 2),
}


NUM_PAD = {
    'X': (0, 0),
    '0': (0, 1),
    'A': (0, 2),
    '1': (1, 0),
    '2': (1, 1),
    '3': (1, 2),
    '4': (2, 0),
    '5': (2, 1),
    '6': (2, 2),
    '7': (3, 0),
    '8': (3, 1),
    '9': (3, 2),
}

GRAPHS = [NUM_PAD, DIR_PAD]


@cache
def get_sequence_len(code, depth, graph):
    if depth == 0:
        return len(code) - 1

    best_len = 0
    for s, e in zip(code, code[1:]):
        cur_graph = GRAPHS[graph]
        s_row, s_col = cur_graph[s]
        e_row, e_col = cur_graph[e]
        row_diff = e_row - s_row
        col_diff = e_col - s_col

        if row_diff < 0:
            row_path = 'd' * -row_diff
        else:
            row_path = 'u' * row_diff
        if col_diff < 0:
            col_path = 'l' * -col_diff
        else:
            col_path = 'r' * col_diff

        paths = set()
        if (e_row, s_col) != cur_graph['X']:
            paths.add('A' + row_path + col_path + 'A')
        if (s_row, e_col) != cur_graph['X']:
            paths.add('A' + col_path + row_path + 'A')

        best_len += min(get_sequence_len(path, depth - 1, graph=1)
                        for path in paths)

    return best_len


def get_complexity(codes, depth):
    return sum(get_sequence_len('A' + code, depth, graph=0) * int(code[:3]) for code in codes)


def main():
    with open(sys.argv[1]) as f:
        codes = [line.strip() for line in f.readlines()]
    print(get_complexity(codes, 3))
    print(get_complexity(codes, 26))


if __name__ == '__main__':
    main()
