from functools import cmp_to_key

dataA, dataB = open(0).read().split("\n\n")

rules = [(*map(int, line.split("|")),) for line in dataA.splitlines()]
manual = [[*map(int, line.split(","))] for line in dataB.splitlines()]
cmp = cmp_to_key(lambda a, b: -((a, b) in rules))


def part1():
    return sum(
        pagelist[len(pagelist) // 2]  # Middle element
        for pagelist in manual  # Of any pagelist
        if pagelist == sorted(pagelist, key=cmp)  # If it's sorted
    )


def part2():
    return sum(
        pagesort[len(pagelist) // 2]  # Middle element
        for pagelist in manual  # Of any pagelist
        if pagelist != (pagesort := sorted(pagelist, key=cmp))  # If it's not sorted
    )


print(part1())
print(part2())
