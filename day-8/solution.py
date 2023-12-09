import re
from math import lcm


def get_input():
    lines = []
    with open('input') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            lines.append(line)

    edges = {}

    ins_mapper = {'L': 0, 'R': 1}

    instructions = [ins_mapper[ins] for ins in lines[0]]

    for l in lines[1:]:
        edge = re.findall(r'\w+', l)
        edges[edge[0]] = [edge[1], edge[2]]

    return instructions, edges


def get_steps_for_node(node, instructions, edges):
    i, s = 0, 0
    while not node.endswith('Z'):
        node = edges[node][instructions[i]]
        i = (i + 1) % len(instructions)
        s += 1

    return node, s


def part1(input):
    instructions, edges = input
    s = get_steps_for_node('AAA', instructions, edges)[1]
    return s


def part2(input):
    instructions, edges = input
    all_nodes = [k for k in edges.keys() if k.endswith('A')]
    res = 1
    # Assumption: nodeCycleLength == nodeCycleOffset (turns out it is correct)
    # we can just find the common multiple off all cycles steps

    for node in all_nodes:
        last_node, steps = get_steps_for_node(node, instructions, edges)
        res = lcm(res, steps)

    return res


inp = get_input()
print('Part 1:', part1(inp))
print('Part 2:', part2(inp))
