from collections import Counter
from functools import cmp_to_key


def get_input():
    lines = []

    with open('input') as file:
        for line in file:
            # 7: AAAAA = A:5
            # 6: AAAAB = A:4, B: 1, AAAAJ, JJJJA
            # 5: AAABB = A:3, B: 2, AAAJJ, JJJAA
            # 4: AAABC = A:3, B: 1, C: 1, JJJBC => BBBBC, AAAJB => AAAAB
            # 3: AABBC = A:2, B: 2, C: 1, AAJJC => AAAAC, AABBJ => AAABB,
            # 2: AABCD = A:2, B: 1, C: 1, D: 1, JJBCD => BBBCD, AAJCD => AAACD
            # 1: ABCDE = ABCDE
            types = []
            line = line.strip().split(' ')
            hand = line[0]
            c = Counter(hand)
            size = len(c)

            jokers = c['J']
            def get_type():
                if size == 1:
                    return 7, 7
                if size == 5:
                    return 1, 1 if jokers == 0 else 2
                if size == 2:
                    if c.most_common(1)[0][1] == 4:
                        return 6, 6 if jokers == 0 else 7
                    else:
                        return 5, 5 if jokers == 0 else 7
                if size == 3:
                    if c.most_common(1)[0][1] == 3:
                        return 4, 4 if jokers == 0 else 6
                    else:
                        return 3, 3 + (0 if jokers == 0 else jokers + 1)

                return 2, 2 if jokers == 0 else 4

            type = get_type()
            bid = int(line[1])

            lines.append((hand, bid, type))

    return lines


def comp(item1, item2, higher_cards, part):
    def resolve_card(card):
        if card.isalpha():
            return higher_cards[card]

        return int(card)

    if item1[2][part] > item2[2][part]:
        return 1
    elif item1[2][part] < item2[2][part]:
        return -1

    for i in range(len(item1[0])):
        card1 = resolve_card(item1[0][i])
        card2 = resolve_card(item2[0][i])

        if card1 > card2:
            return 1
        elif card1 < card2:
            return -1

    return 0


def solve(input, higher_cards, part):
    input.sort(key=cmp_to_key(lambda item1, item2: comp(item1, item2, higher_cards, part)))
    return sum(input[i][1] * (i + 1) for i in range(len(input)))


def part1(input):
    higher_cards = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10}
    return solve(input, higher_cards, 0)


def part2(input):
    higher_cards = {'A': 14, 'K': 13, 'Q': 12, 'J': 1, 'T': 10}
    return solve(input, higher_cards, 1)


inp = get_input()
print('Part 1:', part1(inp))
print('Part 2:', part2(inp))
