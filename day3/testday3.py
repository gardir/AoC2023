from tester import testbase
from day3 import extract_part_numbers


def testpart1():
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
    expected = ("467", "35", "633", "617", "592", "755", "664", "598")
    testbase.test(extract_part_numbers, [(test_input, expected)])


if __name__ == '__main__':
    testpart1()
