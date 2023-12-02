def get_input() -> list[str]:
    with open('input') as file:
        lines = [line.strip() for line in file]

    print(lines)
    return lines


def get_next_digit_p1(a, rev):
    return next(filter(lambda s: s.isdigit(), a))


def get_next_digit_p2(a, rev):
    digits = [(3, {'one': '1', 'two': '2', 'six': '6'}), (4, {'four': '4', 'five': '5', 'nine': '9'}), (5, {'three': '3', 'seven': '7', 'eight': '8'})]

    for i in range(len(a)):
        if a[i].isdigit():
            return a[i]

        for x, m in digits:
            c = a[i: i + x]
            cut = c if not rev else c[::-1]
            if cut in m:
                return m[cut]

    return None


def solve(document, get_next_digit):
    return sum(int(get_next_digit(value, False) + get_next_digit(value[::-1], True)) for value in document)


def part1(document):
    return solve(document, get_next_digit_p1)


def part2(document):
    return solve(document, get_next_digit_p2)


inp = get_input()
print('Part 1:', part1(inp))
print('Part 2:', part2(inp))
