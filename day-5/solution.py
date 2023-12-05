import re
from collections import deque


def get_input():
    lines = []
    converters = []
    with open('input') as file:
        lines = [line.strip() for line in file if line.strip()]

    converter_map = []
    seeds = list(map(int, re.findall(r'\d+', lines[0])))

    for i in range(2, len(lines)):
        line = lines[i]
        if 'map' in line:
            converters.append(converter_map)
            converter_map = []
            continue

        conv = list(map(int, re.findall(r'\d+', line)))
        conv[2] = conv[1] + (conv[2] - 1)  # decresase offset
        converter_map.append(conv)

    converters.append(converter_map)

    return seeds, converters


def part1(input):
    seeds, converters = input

    def convert_seed(seed, converter):

        for interval in converter:
            dest, source_start, source_end = interval
            if source_start <= seed <= source_end:
                dest_offset = seed - source_start
                return dest + dest_offset

        return seed


    for converter in converters:
        new_seeds = []
        for i in range(len(seeds)):
            new_seeds.append(convert_seed(seeds[i], converter))
        seeds = new_seeds

    return min(seeds)


def part2(input):
    seeds, converters = input
    seed_intervals = []

    for i in range(0, len(seeds), 2):
        seed_intervals.append([seeds[i], seeds[i] + (seeds[i + 1] - 1)])

    def get_converted_seed_intervals(current_seed_interval, converter):
        res = []
        next_seed_intervals = [current_seed_interval]

        for interval in converter:
            dest, interval_start, interval_end = interval

            new_seed_intervals = []

            for seed_start, seed_end in next_seed_intervals:
                intersection_start = max(seed_start, interval_start)
                intersection_end = min(seed_end, interval_end)
                if intersection_start > intersection_end:
                    new_seed_intervals.append([seed_start, seed_end])
                    continue

                offset_start = intersection_start - interval_start
                offset_end = intersection_end - interval_start

                res.append([dest + offset_start, dest + offset_end])

                if seed_start < intersection_start:
                    new_seed_intervals.append([seed_start, interval_start - 1])

                if seed_end > intersection_end:
                    new_seed_intervals.append([intersection_end + 1, seed_end])

            next_seed_intervals = new_seed_intervals

        res += next_seed_intervals
        return res

    for converter in converters:
        new_seed_intervals = []
        for seed_interval in seed_intervals:
            new_seed_intervals += get_converted_seed_intervals(seed_interval, converter)

        seed_intervals = new_seed_intervals

    return min(seed[0] for seed in seed_intervals)


inp = get_input()
print('Part 1:', part1(inp))
print('Part 2:', part2(inp))
