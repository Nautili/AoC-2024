import sys
from collections import defaultdict


def get_next_secret_number(s):
    mask = (1 << 24) - 1
    s = ((s << 6) ^ s) & mask
    s = ((s >> 5) ^ s)
    s = ((s << 11) ^ s) & mask
    return s


def get_secret_num_sum(vals, n):
    total = 0
    for val in vals:
        for _ in range(n):
            val = get_next_secret_number(val)
        total += val
    return total


def get_best_sequence(s, n, counts):
    seen_sequences = set()
    cur_key = 0
    cur_val = s % 10
    for i in range(n):
        s = get_next_secret_number(s)
        cur_diff = ((s % 10) - cur_val) & 0b11111
        cur_key = (cur_key >> 5) | (cur_diff << 15)
        cur_val = s % 10

        if i >= 3 and cur_key not in seen_sequences:
            seen_sequences.add(cur_key)
            counts[cur_key] += cur_val


def get_best_sequences(vals, n):
    counts = defaultdict(int)
    for val in vals:
        get_best_sequence(val, n, counts)
    return max(counts.values())


def main():
    with open(sys.argv[1]) as f:
        vals = [int(val.strip()) for val in f.readlines()]
    print(get_secret_num_sum(vals, 2000))
    print(get_best_sequences(vals, 2000))


if __name__ == '__main__':
    main()
