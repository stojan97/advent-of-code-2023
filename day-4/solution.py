import re


def get_input():
    lines = []
    with open('input') as file:
        for line in file:
            line = line.strip()
            winning, your_card = line.split(':')[1].split('|')
            winning = set(map(int, re.findall(r'\d+', winning.strip())))
            your_card = set(map(int, re.findall(r'\d+', your_card.strip())))
            lines.append((winning, your_card))

    return lines


def get_matching(cards):
    card_score = []

    for i, (winning, your_card) in enumerate(cards):
        intersection = winning.intersection(your_card)
        card_score.append(len(intersection))

    return card_score


def part1(cards):
    return sum(int(2 ** (matching - 1)) for matching in get_matching(cards))


def part2(cards):
    matching = get_matching(cards)
    card_count = [1] * len(cards)

    for i in range(len(cards)):
        for j in range(i + 1, i + matching[i] + 1):
            card_count[j] += card_count[i]

    return sum(card_count)


inp = get_input()
print('Part 1:', part1(inp))
print('Part 2:', part2(inp))
