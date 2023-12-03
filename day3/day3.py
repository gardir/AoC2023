import re


def part1(input_file):
    part_numbers = extract_part_numbers(input_file.readlines())
    return sum(map(int, part_numbers.values()))


def is_valid_number(line, number, index):
    end = 0
    checked_all = False
    while not checked_all:
        try:
            start = line.index(number, end)
            end = start + len(number)
            within = start-1 <= index <= end
            if within:
                return True
        except ValueError:
            checked_all = True
            return False
    return False


def explore(schematic, row_index, column):
    numbers = {}
    pattern = re.compile(r"(\d+)")
    min_row, max_row = 0, len(schematic)-1
    if min_row < row_index:
        above_row_index = row_index - 1
        above_row = schematic[above_row_index]
        above_row_numbers = re.findall(pattern, above_row)
        for number in above_row_numbers:
            if is_valid_number(above_row, number, column):
                numbers[(above_row_index, above_row.index(number))] = number
    if row_index < max_row:
        below_row_index = row_index + 1
        below_row = schematic[below_row_index]
        below_row_numbers = re.findall(pattern, below_row)
        for number in below_row_numbers:
            if is_valid_number(below_row, number, column):
                numbers[(below_row_index, below_row.index(number))] = number

    row = schematic[row_index]
    row_numbers = re.findall(pattern, row)
    for number in row_numbers:
        if is_valid_number(row, number, column):
            numbers[(row_index, row.index(number))] = number
    return numbers




def extract_part_numbers(schematic):
    part_numbers = {}
    numerics = set()
    symbols = set()
    for row_index, line in enumerate(schematic):
        for i, symbol in enumerate(line):
            if symbol != '.':
                try:
                    v = int(symbol)
                    numerics.add(v)
                except ValueError:
                    symbols.add(symbol)
                    numbers = explore(schematic, row_index, i)
                    if numbers:
                        part_numbers.update(numbers)
    print(numerics)
    print(symbols)
    return part_numbers


if __name__ == '__main__':
    inputfilename = 'input'
    with open(inputfilename) as f:
        answer = part1(f)
    print(answer)
