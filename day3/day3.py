import re


def part1(input_file):
    part_numbers = extract_part_numbers(input_file.readlines())
    return sum(map(int, part_numbers.values()))


def valid_numbers(number, index):
    try:
        start = number.start()
        end = number.end()
        within = start - 1 <= index <= end
        if within:
            return [start]
    except ValueError:
        pass
    return []


def explore(schematic, row_index, symbol_column):
    numbers = {}
    pattern = re.compile(r"(\d+)")
    min_row, max_row = 0, len(schematic)-1
    if min_row < row_index:
        above_row_index = row_index - 1
        above_row = schematic[above_row_index]
        above_row_numbers = re.finditer(pattern, above_row)
        for number in above_row_numbers:
            columns = valid_numbers(number, symbol_column)
            for column in columns:
                numbers[(above_row_index, column)] = number.group()
    if row_index < max_row:
        below_row_index = row_index + 1
        below_row = schematic[below_row_index]
        below_row_numbers = re.finditer(pattern, below_row)
        for number in below_row_numbers:
            columns = valid_numbers(number, symbol_column)
            for column in columns:
                numbers[(below_row_index, column)] = number.group()

    row = schematic[row_index]
    row_numbers = re.finditer(pattern, row)
    for number in row_numbers:
        columns = valid_numbers(number, symbol_column)
        for column in columns:
            numbers[(row_index, column)] = number.group()
    return numbers


def extract_part_numbers(schematic, verbose=False):
    part_numbers = {}
    numerics = set()
    symbols = set()
    for row_index, line in enumerate(schematic):
        for i, symbol in enumerate(line):
            if symbol != '.' and symbol != '\n':
                try:
                    v = int(symbol)
                    numerics.add(v)
                except ValueError:
                    symbols.add(symbol)
                    numbers = explore(schematic, row_index, i)
                    if numbers:
                        part_numbers.update(numbers)
    if verbose:
        print(numerics)
        print(symbols)
    return part_numbers


if __name__ == '__main__':
    inputfilename = 'input'
    with open(inputfilename) as f:
        answer = part1(f)
    print(f"{answer} (=? 522726)")
