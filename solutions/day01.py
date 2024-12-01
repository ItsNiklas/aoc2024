from collections import Counter

data = open(0).readlines()
inpa, inpb = zip(*map(lambda x: [int(i) for i in x.split()], data))
inpa, inpb = sorted(inpa), sorted(inpb)


def part1():
    return sum(abs(a - b) for a, b in zip(inpa, inpb))


def part2():
    c = Counter(inpb)
    return sum(a * c[a] for a in inpa)


print(part1())
print(part2())
