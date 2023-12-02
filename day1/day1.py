import re


def process_line(line : str):
    pattern = "^\D*(\d).*?(\d?)\D*$"
    l, r = re.findall(pattern, line)[0]
    return int(l+r) if r else int(l+l)


word_conversion = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}


def process_line2(line : str):
    pattern = re.compile(
        r".*?(one|two|three|four|five|six|seven|eight|nine|\d)?(?(1).*(one|two|three|four|five|six|seven|eight|nine|\d)|(one|two|three|four|five|six|seven|eight|nine|\d))")
    all = re.findall(pattern, line)
    leftmost, rightmost, single = all[0]
    if single:
        l = word_conversion.get(single, single)
    else:
        l = word_conversion.get(leftmost, leftmost)
    r = word_conversion.get(rightmost, rightmost)
    return int(l+r) if r else int(l+l)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    filename = 'input'
    s = 0
    with open(filename) as f:
        for l in f:
            s += process_line2(l)
    print(s)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
