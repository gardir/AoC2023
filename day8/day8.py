from threading import Thread, Lock
import re

path_re = re.compile(r"([A-Z]{3}) = \(([A-Z]{3}), ([A-Z]{3})\)")

real = 'input'
example = 'example2'
directions = {'L': 0, 'R': 1}


def check_steps(steps):
    initial = set(steps[0])
    for step in steps[1:]:
        initial = initial.intersection(set(step))
    return initial


if __name__ == '__main__':
    # info('main line')
    with open(real) as f:
        instructions = f.readline().rstrip()
        f.readline()
        paths = {}
        all_starts = []
        for line in f.readlines():
            path, left, right = re.match(path_re, line.rstrip()).groups()
            paths[path] = (left, right)
            if path[-1] == 'A':
                all_starts.append(path)
        step = 0
        print(f"{len(all_starts)} paths to run concurrently")
        lock = Lock()
        steps = [[] for _ in range(len(all_starts))]

        def add_step(i, step):
            lock.acquire()
            try:
                steps[i].append(step)
                return check_steps(steps)
            finally:
                lock.release()

        def explore_paths(i):
            step = 0
            start = all_starts[i]
            path = start
            cycler = [start]
            while True:
                direction = directions[instructions[step % len(instructions)]]
                path = paths[path][direction]
                cycler.append(path)
                if path in cycler and len(cycler) > len(instructions):
                    print(f"It took [{i}] {step} steps to reach a complete 'cycle': {steps[i]}, and cycle {cycler}")
                    break
                step += 1
                if path[-1] == 'Z':
                    if add_step(i, step):
                        break
                elif path == start:
                    print(f"It took [{i}] {steps} steps to 'cycle': {steps[i]}")
                    break

        threads = []
        for i in range(len(all_starts)):
            p = Thread(target=explore_paths, args=(i,))
            p.start()
            threads.append(p)
        for p in threads:
            p.join()
        print(f"It took '{check_steps(steps)}' steps to reach all ending in 'Z': {all_starts}")
