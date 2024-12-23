from collections import defaultdict
from itertools import combinations


data = open(0).read().splitlines()
graph = defaultdict(set)
for line in data:
    a, b = line.split("-")
    graph[a].add(b)
    graph[b].add(a)


def components(comp_size):
    return {
        tuple(sorted(cands))
        for node in graph
        for cands in combinations(graph[node] | {node}, comp_size)
        if all(all(x in graph[y] for x in cands if x != y) for y in cands)
    }


def part1():
    return sum(any(x[0] == "t" for x in comp) for comp in components(3))


def part2():
    return ",".join(*components(max(map(len, graph.values()))))


print(part1())
print(part2())
