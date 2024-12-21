from functools import cache
from itertools import pairwise


data = open(0).read()
inp = data.splitlines()

G = {
    "A": (2, 1),
    "0": (1, 1),
    "1": (0, 2),
    "2": (1, 2),
    "3": (2, 2),
    "4": (0, 3),
    "5": (1, 3),
    "6": (2, 3),
    "7": (0, 4),
    "8": (1, 4),
    "9": (2, 4),
    "^": (1, 1),
    "<": (0, 0),
    "v": (1, 0),
    ">": (2, 0),
}


@cache
def move(p, q, r):
    (x0, y0), (x1, y1) = p, q
    dx, dy = x1 - x0, y1 - y0

    if r == 1:
        return abs(dx) + abs(dy) + 1

    res1, res2 = float("inf"), float("inf")
    lr = ">" * dx if dx > 0 else "<" * abs(dx)
    ud = "^" * dy if dy > 0 else "v" * abs(dy)

    if not (x1 == 0 and y0 == 1):
        code = "A" + lr + ud + "A"
        res1 = sum(move(G[c], G[d], r - 1) for c, d in pairwise(code))

    if not (x0 == 0 and y1 == 1):
        code = "A" + ud + lr + "A"
        res2 = sum(move(G[c], G[d], r - 1) for c, d in pairwise(code))

    return min(res1, res2)


def part1():
    return sum(
        sum(move(G[c], G[d], 3) for c, d in pairwise("A" + code)) * int(code[:-1])
        for code in inp
    )


def part2():
    return sum(
        sum(move(G[c], G[d], 26) for c, d in pairwise("A" + code)) * int(code[:-1])
        for code in inp
    )


print(part1())
print(part2())
