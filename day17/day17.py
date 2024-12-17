import sys
from collections import deque


def combo(op, regs):
    if 4 <= op <= 6:
        return regs[op - 4]
    return op


def run_program(mem, regs):
    pc = 0
    output = []

    while pc < len(mem):
        c_val = combo(mem[pc + 1], regs)
        match mem[pc]:
            case 0:  # adv
                regs[0] = regs[0] >> c_val
            case 1:  # bxl
                regs[1] ^= mem[pc + 1]
            case 2:  # bst
                regs[1] = c_val & 0x7
            case 3:  # jnz
                if regs[0] != 0:
                    pc = mem[pc + 1] - 2
            case 4:  # bxc
                regs[1] ^= regs[2]
            case 5:  # out
                output += [c_val & 0x7]
            case 6:  # bdv
                regs[1] = regs[0] >> c_val
            case 7:  # cdv
                regs[2] = regs[0] >> c_val
        pc += 2
    return output


def find_quine(program):
    pending = deque()
    pending.append(0)

    while pending:
        a = pending.popleft() << 3
        for val in range(a, a + 8):
            out = run_program(program, [val, 0, 0])
            if out[0] == program[-len(out)]:
                if out == program:
                    return val
                pending.append(val)


def main():
    with open(sys.argv[1]) as f:
        lines = [line.strip() for line in f.readlines()]
    program = [int(val) for val in lines[-1].split()[1].split(',')]
    registers = [int(line.split()[2]) for line in lines[:3]]
    print(','.join(str(val) for val in run_program(program, registers)))
    print(find_quine(program))


if __name__ == '__main__':
    main()
