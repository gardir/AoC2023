import re

path_re = re.compile(r"(\w+) = \((\w+), (\w+)\)")

real = 'input'
exampel = 'example'
direction = {'L': 0, 'R': 1}

with open(real) as f:
    instructions = f.readline().rstrip()
    f.readline()
    paths = {}
    for line in f.readlines():
        print(f"'{line}'")
        path, left, right = re.match(path_re, line.rstrip()).groups()
        paths[path] = (left, right)
    print(paths)
    current = 'AAA'
    step = 0
    while current != 'ZZZ':
        current = paths[current][direction[instructions[step % len(instructions)]]]
        step += 1
    print(step)
