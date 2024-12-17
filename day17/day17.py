import sys
from collections import deque


def combo(op, regs):
    if op <= 3:
        return op
    return regs[op - 4]


def run_program(mem, regs):
    ip = 0
    output = []

    while ip < len(mem):
        match mem[ip]:
            case 0:  # adv
                regs[0] = regs[0] >> combo(mem[ip + 1], regs)
            case 1:  # bxl
                regs[1] ^= mem[ip + 1]
            case 2:  # bst
                regs[1] = combo(mem[ip + 1], regs) % 8
            case 3:  # jnz
                if regs[0] != 0:
                    ip = mem[ip + 1] - 2
            case 4:  # bxc
                regs[1] ^= regs[2]
            case 5:  # out
                output += [combo(mem[ip + 1], regs) % 8]
            case 6:  # bdv
                regs[1] = regs[0] >> combo(mem[ip + 1], regs)
            case 7:  # cdv
                regs[2] = regs[0] >> combo(mem[ip + 1], regs)
        ip += 2
    return output


def find_quine(program):
    pending = deque()
    pending.append((len(program) - 1, 0))

    while pending:
        cur_ord, a = pending.popleft()
        for val in range(a << 3, (a + 1) << 3):
            if run_program(program, [val, 0, 0])[0] == program[cur_ord]:
                if cur_ord == 0:
                    return val
                pending.append((cur_ord - 1, val))


def main():
    with open(sys.argv[1]) as f:
        lines = [line.strip() for line in f.readlines()]
    program = [int(val) for val in lines[-1].split()[1].split(',')]
    registers = [int(line.split()[2]) for line in lines[:3]]
    print(','.join(str(val) for val in run_program(program, registers)))
    print(find_quine(program))


if __name__ == '__main__':
    main()
