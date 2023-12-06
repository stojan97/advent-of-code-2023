import math
import re
import time


def get_input():
    times_dist = []
    with open('input') as file:
        lines = [line.strip() for line in file]

    times = list(map(int, re.findall(r'\d+', lines[0])))
    record_dist = list(map(int, re.findall(r'\d+', lines[1])))

    return list(zip(*[times, record_dist]))


def get_how_many_ways(time, record):
    def has_new_record(t):
        remaining_time = time - t
        distance_traveled = remaining_time * t

        return distance_traveled > record

    if not has_new_record(time // 2):
        return 0

    # low
    low, high = 0, time // 2

    while low < high:
        mid = (low + high) // 2

        if not has_new_record(mid):
            low = mid + 1
        else:
            high = mid

    start = low
    mid = time // 2 + (0 if time % 2 == 0 else 1)
    end = mid + ((time // 2) - start)

    return end - start + 1


def part1(races):
    return math.prod(get_how_many_ways(time, record) for time, record in races)


def part2(races):
    time = int(''.join([str(r[0]) for r in races]))
    record = int(''.join([str(r[1]) for r in races]))
    return get_how_many_ways(time, record)


inp = get_input()
print('Part 1:', part1(inp))
print('Part 2:', part2(inp))
