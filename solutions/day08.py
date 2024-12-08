from collections import defaultdict
from itertools import permutations

data = open(0).readlines()
freqs = defaultdict(list)

for i, line in enumerate(data):
    for j, c in enumerate(line):
        if c != ".":
            freqs[c].append(complex(i, j))

N, M = len(data[0].strip()), len(data)


def part1():
    return len(
        {
            α - (β - α)  # Antinode position
            for freq_locs in freqs.values()  # For all the different frequencies
            for α, β in permutations(freq_locs, 2)  # For all pairs
            if 0 <= (α - (β - α)).real < M and 0 <= (α - (β - α)).imag < N
        }
    )


def part2():
    return len(
        {
            α + k * (β - α)  # Antinode position
            for freq_locs in freqs.values()  # For all the different frequencies
            for α, β in permutations(freq_locs, 2)  # For all unique pairs
            for k in range(min(N, M))  # All possible antinode offsets
            if 0 <= (α + k * (β - α)).real < M and 0 <= (α + k * (β - α)).imag < N
        }
    )


print(part1())
print(part2())
