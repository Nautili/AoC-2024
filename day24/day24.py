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


def to_gate_id(val):
    id = str(val)
    if len(id) < 2:
        id = '0' + id
    return id


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


def get_bad_gates(gates):
    # clear gates
    input_len = 0
    for name, gate in gates.items():
        if name[0] in 'xy':
            input_len = max(input_len, int(name[1:]))
            gate.value = 0

    # flip one bit at a time
    bad_gates = set()
    for i in range(input_len + 1):
        id = to_gate_id(i)

        gates['x' + id].value = 1
        if propagate(gates) != (1 << i):
            bad_gates.add(i)
        gates['x' + id].value = 0

    return list(bad_gates)


def find_carry_name(gates, bad_gate):
    prev_out = 'z' + to_gate_id(bad_gate - 1)
    if prev_out not in gates:
        return None

    prev_inputs = set(gates[prev_out].inputs)
    for add_carry, add_gate in gates.items():
        if add_carry != prev_out and set(add_gate.inputs) == prev_inputs:
            for out_carry, out_gate in gates.items():
                if add_carry in out_gate.inputs:
                    return out_carry


def find_other_input(gates, known_gate, target_type):
    for gate in gates.values():
        if gate.type == target_type and known_gate in gate.inputs:
            for input in gate.inputs:
                if input != known_gate:
                    return input


def find_out_gate(gates, inputs, target_type):
    for name, gate in gates.items():
        if gate.type == target_type and set(inputs) == set(gate.inputs):
            return name


def fix_half_adder(gates, bad_gate):
    raw_inputs = [prefix + to_gate_id(bad_gate) for prefix in 'xy']
    maybe_one_bit = find_out_gate(gates, raw_inputs, GateType.XOR)
    prev_carry = find_carry_name(gates, bad_gate)

    # handle case where first gate is bad
    if not prev_carry:
        return [maybe_one_bit, 'z' + to_gate_id(bad_gate)]

    one_bit = find_other_input(gates, prev_carry, GateType.XOR)
    maybe_zout = find_out_gate(gates, [one_bit, prev_carry], GateType.XOR)
    # handle case where out gate has swapped
    if maybe_zout[0] != 'z':
        return [maybe_zout, 'z' + to_gate_id(bad_gate)]

    # handle case where single bit addition gate is swapped
    if one_bit != maybe_one_bit:
        return [maybe_one_bit, one_bit]


def get_swapped_gates(gates):
    bad_gates = get_bad_gates(gates)
    swaps = []
    for bad_gate in bad_gates:
        swaps += fix_half_adder(gates, bad_gate)
    swaps = [val for val in swaps if val is not None]
    return ','.join(sorted(swaps))


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
    print(get_swapped_gates(gates))


if __name__ == '__main__':
    main()
