from day1 import process_line2

def test1():
    print("Testing)")
    tests = [
        ("1abc2", 12),
        ("pqr3stu8vwx", 38),
        ("a1b2c3d4e5f", 15),
        ("treb7uchet", 77)
    ]
    results = []
    for param, expected in tests:
        actual = process_line(param)
        if actual == expected:
            results.append(f"process_line({param}) -- OK!")
        else:
            results.append(f"process_line({param}) -- '{actual}' != {expected} (expected)")
    print('\n'.join(results))


def test2():
    tests = [
        ("two1nine", 29),
        ("eightwothree", 83),
        ("abcone2threexyz", 13),
        ("xtwone3four", 24),
        ("4nineeightseven2", 42),
        ("zoneight234", 14),
        ("7pqrstsixteen", 76),
        ("wqnwqrqnwrnwonewnqnwqenwqe", 11),
    ]
    results = []
    for param, expected in tests:
        try:
            actual = process_line2(param)
        except Exception as e:
            actual = e
        if actual == expected:
            results.append(f"process_line({param}) -- OK!")
        else:
            results.append(f"process_line({param}) -- '{actual}' != {expected} (expected)")
    print('\n'.join(results))

test2()