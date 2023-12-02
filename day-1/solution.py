def get_input():
    with open('sample') as file:
        lines = [line.strip() for line in file]

    print(lines)
    return lines


def part1(input):
    pass


def part2(input):
    pass


inp = get_input()
print('Part 1:', part1(inp))
print('Part 2:', part2(inp))
