import re

example_input = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11""".split("\n")

digits = re.compile(r"(\d+)")


def part1(lotterypile):
    total_points = 0
    for line in lotterypile:
        line = line.split(":")[1]
        winning_numbers, my_hand = line.split("|")
        winning_numbers = set(re.findall(digits, winning_numbers))
        my_numbers = set(re.findall(digits, my_hand))
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


if __name__ == '__main__':
    inputfilename = 'input'
    with open(inputfilename) as f:
        answer = part1(f.readlines())
    print(f"{answer}")
