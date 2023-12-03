from tester import testbase
from day3 import extract_part_numbers, explore, is_valid_number, part1


def testpart1():
    is_valid_number_cases = (
        (("467..114..", "467", 3), True),
        (("467..114..", "114", 3), False),
         #"...*......",
        (("..35..633.", "35", 3), True),
        (("..35..633.", "633", 3), False),
         #"......#...",
        (("..35..633.", "35", 6), False),
        (("..35..633.", "633", 6), True),
        (("617*......", "617", 3), True),
        (("617*......", "617", 5), False),
         #".....+.58.",
        ((".....+.58.", "58", 5), False),
        (("..592.....", "592", 5), True),
        (("......755.", "755", 3), False),
        (("......755.", "755", 5), True),
         #"...$.*....",
        ((".664.598..", "664", 3), True),
        ((".664.598..", "664", 5), False),
        ((".664.598..", "598", 3), False),
        ((".664.598..", "598", 5), True),
        ## PERSONAL TESTS
        ((".664.664..", "664", 5), True),
    )
    testbase.test(is_valid_number, is_valid_number_cases)
    expected_exctraction = {
        (0, 0): "467",
        (2, 2): "35",
        (2, 6): "633",
        (4, 0): "617",
        (6, 2): "592",
        (7, 6): "755",
        (9, 1): "664",
        (9, 5): "598",
    }
    test_input = [
        "467..114..",
        "...*......",
        "..35..633.",
        "......#...",
        "617*......",
        ".....+.58.",
        "..592.....",
        "......755.",
        "...$.*....",
        ".664.598..",
    ]
    expected_numbers_from_symbols = [
        # explore(schematic, row, column)
        ((test_input, 1, 3), {(0, 0): "467", (2, 2): "35"}),
        ((test_input, 3, 6), {(2, 6): "633"}),
        ((test_input, 4, 3), {(4, 0): "617"}),
        ((test_input, 5, 5), {(6, 2): "592"}),
        ((test_input, 8, 3), {(9, 1): "664"}),
        ((test_input, 8, 5), {(7, 6): "755", (9, 5): "598"}),
    ]
    testbase.test(explore, expected_numbers_from_symbols)
    testbase.test(extract_part_numbers, [((test_input,), expected_exctraction)])
    part_numbers = extract_part_numbers(test_input)
    part_numbers_sum = sum(map(int, part_numbers.values()))
    expected_sum = 4361
    print(f"expected {expected_sum} =? {part_numbers_sum}?")


if __name__ == '__main__':
    testpart1()
