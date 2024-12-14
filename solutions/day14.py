from math import prod
import re

data = open(0).read().splitlines()
inp = {i: tuple(map(int, re.findall(r"-?\d+", line))) for i, line in enumerate(data)}
xm = (w := 11 if len(inp) <= 12 else 101) // 2
ym = (h := 7 if len(inp) <= 12 else 103) // 2


def part1():
    for _ in range(100):  # Simulate 100 seconds
        for i, (px, py, vx, vy) in inp.items():
            inp[i] = ((px + vx) % w, (py + vy) % h, vx, vy)

    ans = [0] * 4
    for px, py, *_ in inp.values():  # Count each of the quadrants
        ans[0] += px > xm and py > ym
        ans[1] += px < xm and py > ym
        ans[2] += px < xm and py < ym
        ans[3] += px > xm and py < ym

    return prod(ans)


def part2():
    c = lambda p: abs(p[0] - xm) <= 20 and abs(p[1] - ym) <= 20  # Count hits in center
    for k in range(100, 10000):  # 100 seconds have already passed in Part 1
        if sum(map(c, inp.values())) > 290:  # Good threshold to detect the easter egg
            return k

        for i, (px, py, vx, vy) in inp.items():
            inp[i] = ((px + vx) % w, (py + vy) % h, vx, vy)


print(part1())
print(part2())
