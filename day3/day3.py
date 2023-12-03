import re


def part1(input_file):
    part_numbers = extract_part_numbers(input_file.readlines())
    return sum(map(int, part_numbers))


def extract_part_numbers(schematic):
    pattern = re.compile(r"(\d+)")
    numbers = re.findall(pattern, schematic[0])
    return numbers


if __name__ == '__main__':
    inputfilename = 'input'
    with open(inputfilename) as f:
        answer = part1(f)
    print(answer)
