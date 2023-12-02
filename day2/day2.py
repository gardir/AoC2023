import re


def part1(f):
    answer_sum = 0
    # 12 red cubes, 13 green cubes, and 14 blue cubes
    max_red = 12
    max_green = 13
    max_blue = 14
    for game in f:
        game_id, reds, greens, blues = extract_max(game)
        if reds <= max_red and blues <= max_blue and greens <= max_green:
            answer_sum += game_id
    return answer_sum


def part2(f):
    answer_sum = 0
    for game in f:
        game_id, reds, greens, blues = extract_max(game)
        answer_sum += reds * greens * blues
    return answer_sum


def extract(wrapper, game):
    game_id = int(re.findall(re.compile(r"Game (\d+)"), game)[0])
    reds = wrapper(map(int, re.findall(re.compile(r"(\d+) red"), game)))
    greens = wrapper(map(int, re.findall(re.compile(r"(\d+) green"), game)))
    blues = wrapper(map(int, re.findall(re.compile(r"(\d+) blue"), game)))
    return game_id, reds, greens, blues


def extract_max(game):
    return extract(max, game)


def extract_min(game):
    return extract(min, game)


if __name__ == '__main__':
    inputfilename = 'input'
    with open(inputfilename) as f:
        answer = part2(f)
    print(answer)
