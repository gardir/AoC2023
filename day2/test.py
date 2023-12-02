import day2


def test_extract():
    test_cases = (
        ("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green", (1, 4, 2, 6)),
        ("Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue", (2, 1, 3, 4)),
        ("Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red", (3, 20, 13, 6)),
        ("Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red", (4, 14, 3, 15)),
        ("Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green", (5, 6, 3, 2)),
    )
    for params, expected in test_cases:
        try:
            actual = day2.extract_max(params)
        except Exception as e:
            actual = e
        if actual != expected:
            print(f"extract({params}) => {actual} (!= '{expected}')")
        else:
            print(f"extract({params}) => OK !")


if __name__ == '__main__':
    test_extract()
