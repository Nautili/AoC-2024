import sys
import copy


def get_checksum(line):
    out_length = sum(line[::2])
    out_index = 0
    front = 0
    back = len(line) - 1
    total = 0
    while out_index < out_length:
        while out_index < out_length and line[front] > 0:
            total += out_index * (front // 2)
            out_index += 1
            line[front] -= 1
        front += 1
        while out_index < out_length and line[front] > 0:
            total += out_index * (back // 2)
            out_index += 1
            line[front] -= 1
            line[back] -= 1
            if line[back] == 0:
                back -= 2
        front += 1
    return total


def get_block_checksum(line):
    original = copy.copy(line)
    out_index = 0
    front = 0
    total = 0
    while front < len(line):
        if front % 2 == 0:  # process existing block
            out_index += original[front] - line[front]
            while line[front] > 0:
                total += out_index * (front // 2)
                out_index += 1
                line[front] -= 1
        else:  # process gap
            back = len(line) - 1
            while back >= 0 and line[front] > 0:
                while back >= 0 and (line[back] == 0 or line[back] > line[front]):
                    back -= 2
                if back >= 0:
                    while line[back] > 0:
                        total += out_index * (back // 2)
                        out_index += 1
                        line[front] -= 1
                        line[back] -= 1
            out_index += line[front]
        front += 1
    return total


def main():
    with open(sys.argv[1]) as f:
        line = [int(val) for val in f.readline().strip()]
        print(get_checksum(copy.copy(line)))
        print(get_block_checksum(line))


if __name__ == '__main__':
    main()
