from tester import testbase
import day2


def test_extract_max():
    test_cases = (
        ("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green", (1, 4, 2, 6)),
        ("Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue", (2, 1, 3, 4)),
        ("Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red", (3, 20, 13, 6)),
        ("Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red", (4, 14, 3, 15)),
        ("Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green", (5, 6, 3, 2)),
    )
    testbase.test(day2.extract_max, test_cases)


def test_extract_min():
    """
In game 1, the game could have been played with as few as 4 red, 2 green, and 6 blue cubes. If any color had even one fewer cube, the game would have been impossible.
Game 2 could have been played with a minimum of 1 red, 3 green, and 4 blue cubes.
Game 3 must have been played with at least 20 red, 13 green, and 6 blue cubes.
Game 4 required at least 14 red, 3 green, and 15 blue cubes.
Game 5 needed no fewer than 6 red, 3 green, and 2 blue cubes in the bag.
    :return:
    """
    test_cases = (
        ("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green", (1, 4, 2, 6)),
        ("Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue", (2, 1, 3, 4)),
        ("Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red", (3, 20, 13, 6)),
        ("Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red", (4, 14, 3, 15)),
        ("Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green", (5, 6, 3, 2)),
    )
    testbase.test(day2.extract_min, test_cases)


if __name__ == '__main__':
    test_extract_max()
