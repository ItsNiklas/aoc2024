data = open(0).readlines()
reports = [[*map(int, line.split())] for line in data]


def safe(lvls):
    return (
        lvls == sorted(lvls) or lvls[::-1] == sorted(lvls)
        if all(1 <= abs(x - y) <= 3 for x, y in zip(lvls, lvls[1:]))
        else 0
    )


def part1():
    return sum(map(safe, reports))


def part2():
    return sum(
        map(
            lambda lvls: any(safe(lvls[:i] + lvls[i + 1 :]) for i in range(len(lvls))),
            reports,
        )
    )


print(part1())
print(part2())
