from math import log10
from operator import add, mul


data = [[*map(int, line.replace(":", "").split())] for line in open(0)]
cat = lambda a, b: a * 10 ** int(log10(b) + 1) + b


def find_ops(a, b, bs, ops):
    if not bs:
        return a == b
    return any(find_ops(a, nb, bs[1:], ops) for op in ops if (nb := op(b, bs[0])) <= a)


def part1():
    return sum(a for a, *b in data if find_ops(a, b[0], b[1:], (add, mul)))


def part2():
    return sum(a for a, *b in data if find_ops(a, b[0], b[1:], (add, mul, cat)))


print(part1())
print(part2())
