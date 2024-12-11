from functools import cache

data = open(0).read()
inp = [*map(int, data.split())]


@cache
def blink(stone, k):
    if k == 0:
        return 1

    if stone == 0:
        return blink(1, k - 1)
    if len(s := str(stone)) % 2 == 0:
        return blink(int(s[: len(s) // 2]), k - 1) + blink(int(s[len(s) // 2 :]), k - 1)
    return blink(stone * 2024, k - 1)


def part1():
    return sum(blink(stone, 25) for stone in inp)


def part2():
    return sum(blink(stone, 75) for stone in inp)


print(part1())
print(part2())
