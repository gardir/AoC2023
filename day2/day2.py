import re


def parse_file(f):
    id_sum = 0
    # 12 red cubes, 13 green cubes, and 14 blue cubes
    max_red = 12
    max_green = 13
    max_blue = 14
    for game in f:
        game_id, reds, greens, blues = extract_max(game)
        if reds <= max_red and blues <= max_blue and greens <= max_green:
            id_sum += game_id
    return id_sum


def extract_max(game):
    game_id = int(re.findall(re.compile(r"Game (\d+)"), game)[0])
    reds = max(map(int, re.findall(re.compile(r"(\d+) red"), game)))
    greens = max(map(int, re.findall(re.compile(r"(\d+) green"), game)))
    blues = max(map(int, re.findall(re.compile(r"(\d+) blue"), game)))
    return game_id, reds, greens, blues


if __name__ == '__main__':
    inputfilename = 'input'
    with open(inputfilename) as f:
        answer = parse_file(f)
    print(answer)
