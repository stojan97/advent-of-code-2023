import math
import re
from typing import List


def get_input():
    map_color = {'red': 0, 'green': 1, 'blue': 2}

    with open('input') as file:
        lines = []
        for line in file:
            numbers: List[str] = line.split(':')
            split = numbers[1].strip().split(';')
            subsets = []
            for s in split:
                findall = re.findall(r'(\d+) (\w+)', s)
                colors = [0, 0, 0]
                for value, c in findall:
                    colors[map_color[c]] = int(value)

                subsets.append(colors)
            lines.append(subsets)

    return lines


def part1(games):
    limits = [12, 13, 14]

    def is_possible(subsets):
        for s in subsets:
            for i in range(3):
                if s[i] > limits[i]:
                    return False
        return True

    return sum((idx + 1 if is_possible(g) else 0) for idx, g in enumerate(games))


def part2(games):
    def mul_cubes(subsets):
        zipped_subsets = zip(*subsets)
        return math.prod(max(z) for z in zipped_subsets)

    return sum(mul_cubes(g) for g in games)


inp = get_input()
print('Part 1:', part1(inp))
print('Part 2:', part2(inp))
