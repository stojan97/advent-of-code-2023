import math


def get_input():
    grid = []
    numbers = []
    row = 0
    gears = {}
    with open('input') as file:
        for line in file:
            row_numbers = []
            current_number = ''
            line = line.strip()

            curr_gears = {(row, i): set() for i in range(len(line)) if line[i] == '*'}
            gears.update(curr_gears)

            for i in range(len(line)):
                if line[i].isdigit():
                    current_number += line[i]
                else:
                    if current_number:
                        row_numbers.append((current_number, row, i - len(current_number)))
                    current_number = ''

            if current_number:
                row_numbers.append((current_number, row, i - len(current_number)))

            numbers += row_numbers
            grid.append(line)
            row += 1

    return grid, numbers, gears


def adj(x, y):
    return [(x - 1, y - 1), (x - 1, y), (x - 1, y + 1), (x, y - 1), (x, y + 1), (x + 1, y - 1), (x + 1, y),
            (x + 1, y + 1)]


def in_range(x, y, rows, cols):
    return 0 <= x < rows and 0 <= y < cols


def part1(input):
    grid, numbers, _ = input

    def get_sum(number, i, j):
        rows = len(grid)
        cols = len(grid[0])

        for col in range(j, j + len(number)):
            for x, y in adj(i, col):
                if in_range(x, y, rows, cols) and grid[x][y] != '.' and not grid[x][y].isdigit():
                    return int(number)

        return 0

    return sum(get_sum(number, i, j) for number, i, j in numbers)


def part2(input):
    grid, numbers, gears = input

    def add_number_to_gear(idx, number, i, j):
        rows = len(grid)
        cols = len(grid[0])

        for col in range(j, j + len(number)):
            for x, y in adj(i, col):
                if in_range(x, y, rows, cols) and grid[x][y] == '*':
                    gears[(x, y)].add(idx)

    for idx, (number, i, j) in enumerate(numbers):
        add_number_to_gear(idx, number, i, j)

    return sum(math.prod([int(numbers[l][0]) for l in list(g)]) for g in gears.values() if len(g) == 2)


inp = get_input()
print('Part 1:', part1(inp))
print('Part 2:', part2(inp))
