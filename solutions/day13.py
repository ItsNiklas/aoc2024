import re

data = open(0).read().split("\n\n")
inp = [(*map(int, re.findall(r"\d+", block)),) for block in data]


def part1():
    ans = 0

    for ax, ay, bx, by, px, py in inp:  # min 3*A + B
        det = ax * by - ay * bx
        A, r1 = divmod(px * by - py * bx, det)  # ax * A + bx * B = px
        B, r2 = divmod(py * ax - px * ay, det)  # ay * A + by * B = py

        ans += 0 if r1 or r2 else 3 * A + B

    return ans


def part2():
    global inp
    inp = [(*v, px + 10000000000000, py + 10000000000000) for *v, px, py in inp]
    return part1()


print(part1())
print(part2())
