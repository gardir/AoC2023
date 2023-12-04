import re

example_input = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11""".split("\n")

card_regex = re.compile(r"Card\s+(\d+):((?:\s+\d+)+) \|((?:\s+\d+)+)")


def part1(lotterypile):
    total_points = 0
    for line in lotterypile:
        card_index, winners, mine = re.match(card_regex, line).groups()
        winning_numbers = set(winners.split())
        my_numbers = set(mine.split())
        intersection = winning_numbers.intersection(my_numbers)
        if len(intersection) == 0:
            points = 0
        else:
            power = len(intersection) - 1
            points = 2 ** power
        total_points += points

    return total_points

# 27072
# 26988
# 26972
# That's not the right answer; your answer is too high.
# 21959 correct!


def part2(lotterypile):
    card_copies = {1: 1}
    current_card_copy = 1
    while current_card_copy <= len(lotterypile):
        if current_card_copy not in card_copies:
            card_copies[current_card_copy] = 1
        card_index, winners, mine = re.match(card_regex, lotterypile[current_card_copy - 1]).groups()
        winning_numbers = set(winners.split())
        my_numbers = set(mine.split())
        intersection = winning_numbers.intersection(my_numbers)
        for i in range(1, len(intersection) + 1):
            card_copy = current_card_copy + i
            if card_copy in card_copies:
                card_copies[card_copy] += card_copies[current_card_copy]
            else:
                card_copies[card_copy] = 1 + card_copies[current_card_copy]
        current_card_copy += 1
    return sum(card_copies.values())

# 3760351
# 5002065
# 5132675 (the cards outside of the limit did count
# That's not the right answer; your answer is too low.


if __name__ == '__main__':
    inputfilename = 'input'
    with open(inputfilename) as f:
        answer = part2(f.readlines())
    print(f"{answer}")
