import re

seed_filter = re.compile(r"(\d+)")
range_filter = re.compile(r"(\d+)\s+(\d+)\s+(\d+)")
phases = [
    "seed-to-soil map:",
    "soil-to-fertilizer map:",
    "fertilizer-to-water map:",
    "water-to-light map:",
    "light-to-temperature map:",
    "temperature-to-humidity map:",
    "humidity-to-location map:"
]
range_maps = {k: [] for k in phases}


class Range:

    def __init__(self, destination, source, range):
        self.source = source
        self.destination = destination
        self.range = range

    def convert(self, number):
        if self.source <= number < self.source + self.range:
            index = number - self.source
            return self.destination + index
        return False

    def __repr__(self):
        return f"R{{{self.source} {self.destination} {self.range}}}"

    def __str__(self):
        return f"R{{{self.source} {self.destination} {self.range}}}"


def part1(infile):
    seeds = list(map(int, re.findall(seed_filter, infile.readline())))
    return find_closest_location(infile, seeds)


def part2(infile):
    seeds = re.findall(seed_filter, infile.readline())
    class Seed():

        def __iter__(self):
            for seed_start, seed_range in zip(seeds[::2], seeds[1::2]):
                start = int(seed_start)
                end = start + int(seed_range)
                for seed in range(start, end):
                    yield seed
    return find_closest_location(infile, Seed())



def find_closest_location(infile, seeds):
    # print(seeds)
    for phase in phases:
        read_ranges(infile, phase)
    # print(range_maps)
    locations = []
    try:
        for seed in seeds:
            # print(f"seed {seed} =>", end='')
            transformation = seed
            for phase in phases:
                phase_range = range_maps[phase]
                for range in phase_range:
                    if range.convert(transformation):
                        transformation = range.convert(transformation)
                        break
                # print(f" ({phase}) {transformation}", end='')
            # print()
            # print(f"seed '{seed}' => '{transformation}'")
            locations.append(transformation)
    except StopIteration:
        pass
    return min(locations)


def read_ranges(infile, phase):
    line = infile.readline().rstrip()
    while line != phase:
        line = infile.readline().rstrip()
    all_ranges_read = False
    range_map = range_maps[phase]
    while not all_ranges_read:
        try:
            source, destination, range = list(map(int, re.match(range_filter, infile.readline()).groups()))
            range_map.append(Range(source, destination, range))
        except AttributeError as e:
            all_ranges_read = True


inputfilename = 'input'
examplefilename = 'example'
with open(inputfilename) as f:
    answer = part2(f)
print(f"{answer}")