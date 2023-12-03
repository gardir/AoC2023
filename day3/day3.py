import re


def part1(input_file):
    part_numbers = extract_part_numbers(input_file.readlines())
    return sum(map(int, part_numbers.values()))


def valid_numbers(line, number, index):
    end = 0
    checked_all = False
    all_numbers = []
    while not checked_all:
        try:
            start = line.index(number, end)
            end = start + len(number)
            within = start-1 <= index <= end
            if within:
                all_numbers.append(start)
        except ValueError:
            checked_all = True
    return all_numbers


def explore(schematic, row_index, symbol_column):
    numbers = {}
    pattern = re.compile(r"(\d+)")
    min_row, max_row = 0, len(schematic)-1
    if min_row < row_index:
        above_row_index = row_index - 1
        above_row = schematic[above_row_index]
        above_row_numbers = re.findall(pattern, above_row)
        for number in above_row_numbers:
            columns = valid_numbers(above_row, number, symbol_column)
            for column in columns:
                numbers[(above_row_index, column)] = number
    if row_index < max_row:
        below_row_index = row_index + 1
        below_row = schematic[below_row_index]
        below_row_numbers = re.findall(pattern, below_row)
        for number in below_row_numbers:
            columns = valid_numbers(below_row, number, symbol_column)
            for column in columns:
                numbers[(below_row_index, column)] = number

    row = schematic[row_index]
    row_numbers = re.findall(pattern, row)
    for number in row_numbers:
        columns = valid_numbers(row, number, symbol_column)
        for column in columns:
            numbers[(row_index, column)] = number
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
