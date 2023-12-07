import numpy as np

puzzle = ["Time:        52     94     75     94",
          "Distance:   426   1374   1279   1216"]

example = ["Time:      7  15   30",
           "Distance:  9  40  200"]

runthrough = puzzle
times = list(map(int, runthrough[0].split()[1:]))
records = list(map(int, runthrough[1].split()[1:]))

time2 = int(''.join(runthrough[0].split()[1:]))
record2 = int(''.join(runthrough[1].split()[1:]))

def wins(time, record):
    return sum(i*(time-i) > record for i in range(time))

print(np.prod([wins(time, record) for time, record in zip(times, records)]))
print(wins(time2, record2))
