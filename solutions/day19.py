from functools import cache

data = open(0).read().splitlines()
parts = data[0].split(", ")
inp = data[2:]


@cache
def count_towel(design):  # Normal dp solution with @cache <3
    if not design:
        return 1

    return sum(count_towel(design[len(t) :]) for t in parts if design.startswith(t))


def part1():
    return sum(bool(count_towel(design)) for design in inp)


def part2():
    return sum(count_towel(design) for design in inp)


print(part1())
print(part2())
