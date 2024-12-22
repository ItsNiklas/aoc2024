from collections import defaultdict


data = open(0).read().splitlines()
inp = [*map(int, data)]


def rng(s, k=2000):
    for _ in range(k):
        s = s ^ s << 6 & 0xFFFFFF
        s = s ^ s >> 5 & 0xFFFFFF
        s = s ^ s << 11 & 0xFFFFFF
        yield s


def part1():
    return sum([*rng(secret)][-1] for secret in inp)


def part2():
    res = defaultdict(int)

    for secret in inp:
        values = [v % 10 for v in rng(secret)]
        diffs = [x - y for x, y in zip(values, values[1:])]

        seen = set()
        for i in range(len(diffs) - 3):
            if (t := tuple(diffs[i : i + 4])) not in seen:
                seen.add(t)
                res[t] += values[i + 4]

    return max(res.values())


print(part1())
print(part2())
