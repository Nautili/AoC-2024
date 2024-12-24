import sys
from enum import Enum
from operator import iand, ior, ixor
from functools import reduce


class GateType(Enum):
    VALUE = 1
    AND = 2
    OR = 3
    XOR = 4


op_map = {GateType.AND: iand, GateType.OR: ior, GateType.XOR: ixor}


class Gate:
    def __init__(self, type=GateType.VALUE, inputs=[], value=None):
        self.inputs = inputs
        self.type = type
        self.value = value

    def get_value(self, gates):
        input_vals = [gates[input].get_value(gates) for input in self.inputs]
        if any(val == None for val in input_vals):
            return None

        if self.type == GateType.VALUE:
            return self.value

        return reduce(op_map[self.type], input_vals)


def propagate(gates):
    evaluated = {}
    z_vals = []
    while len(evaluated) != len(gates):
        for name, gate in gates.items():
            if name not in evaluated and (val := gate.get_value(gates)) != None:
                evaluated[name] = val
                if name[0] == 'z':
                    z_vals.append((name, val))

    return int(''.join(str(val) for _, val in sorted(z_vals))[::-1], 2)


def test_values(gates):
    input_len = 0
    for name, gate in gates.items():
        if name[0] in 'xy':
            input_len = max(input_len, int(name[1:]))
            gate.value = 0

    for i in range(input_len + 1):
        id = str(i)
        if len(id) < 2:
            id = '0' + id
        gates['x' + id].value = 1
        # gates['y' + id].value = 1
        val = propagate(gates)
        if val != 1 << (i):
            print(id, val)
        gates['x' + id].value = 0
        # gates['y' + id].value = 0


def main():
    gates = {}
    with open(sys.argv[1]) as f:
        for line in f.readlines():
            if ':' in line:
                name, val = line.strip().split()
                gates[name[:-1]] = Gate(value=int(val))
            elif '>' in line:
                i1, gate_type, i2, _, name = line.strip().split()
                gates[name] = Gate(type=GateType[gate_type], inputs=[i1, i2])

    print(propagate(gates))
    test_values(gates)


if __name__ == '__main__':
    main()
