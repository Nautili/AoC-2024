import sys
from functools import cache


class Node:
    def __init__(self):
        self.children = {}
        self.end = False

    def print_trie(self, indent=0):
        for child, node in self.children.items():
            print(' ' * indent, child, node.end)
            node.print_trie(indent + 2)


def build_trie(parts):
    root = Node()

    for part in parts:
        cur_node = root
        for c in part:
            if c not in cur_node.children:
                cur_node.children[c] = Node()
            cur_node = cur_node.children[c]
        cur_node.end = True

    return root


@cache
def design_count(trie, cur_node, pattern, idx=0):
    if idx == len(pattern):
        return cur_node == trie
    cur_char = pattern[idx]
    if cur_char not in cur_node.children:
        return 0

    next_node = cur_node.children[cur_char]
    count = design_count(trie, next_node, pattern, idx + 1)
    if next_node.end:
        count += design_count(trie, trie, pattern, idx + 1)

    return count


def get_counts(trie, patterns):
    return [design_count(trie, trie, pattern) for pattern in patterns]


def get_valid_designs(counts):
    return sum(1 for count in counts if count > 0)


def get_all_valid_designs(counts):
    return sum(counts)


def main():
    with open(sys.argv[1]) as f:
        lines = [line.strip() for line in f.readlines()]

    parts = lines[0].split(', ')
    patterns = lines[2:]

    trie = build_trie(parts)

    counts = get_counts(trie, patterns)
    print(get_valid_designs(counts))
    print(get_all_valid_designs(counts))


if __name__ == '__main__':
    main()
