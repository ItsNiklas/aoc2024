import re

data = open(0).read()
matches = re.findall(r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))", data)


def part1():
    return sum(int(a) * int(b) for a, b, *_ in matches if a)


def part2():
    res, active = 0, True

    for a, b, do, dont in matches:
        if do or dont:
            active = bool(do)
        elif active:
            res += int(a) * int(b)

    return res


print(part1())
print(part2())
