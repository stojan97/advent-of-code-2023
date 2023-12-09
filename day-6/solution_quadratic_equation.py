import math
import re


def get_input():
    times_dist = []
    with open('input') as file:
        lines = [line.strip() for line in file]

    times = list(map(int, re.findall(r'\d+', lines[0])))
    record_dist = list(map(int, re.findall(r'\d+', lines[1])))

    return list(zip(*[times, record_dist]))


def get_how_many_ways(time, record):
    # (time - t) * t
    # -t^2 + time*t = record
    # -t^2 + time*t - record = 0
    # x1 = record .... peak .... x2 = record
    # result is equal to
    # x1 + 1 .... peak .... x2 - 1

    a, b, c = -1, time, -record

    d = b ** 2 - 4 * a * c

    x1 = (-b + math.sqrt(d)) / (2 * a) + 1
    x1 = math.floor(x1)
    x2 = (-b - math.sqrt(d)) / (2 * a) - 1
    x2 = math.ceil(x2)
    return x2 - x1 + 1


def part1(races):
    return math.prod(get_how_many_ways(time, record) for time, record in races)


def part2(races):
    time = int(''.join([str(r[0]) for r in races]))
    record = int(''.join([str(r[1]) for r in races]))
    return get_how_many_ways(time, record)


inp = get_input()
print('Part 1:', part1(inp))
print('Part 2:', part2(inp))
