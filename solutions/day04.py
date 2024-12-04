from itertools import product

data = open(0).readlines()
N, M = len(data), len(data[0])
data = {(x, y): data[x][y] for x, y in product(range(N), range(M))}


def part1():
    ans = 0
    deltas = [(0, 1), (1, 0), (1, 1), (1, -1)]

    for i in range(N):
        for j in range(M):
            for dx, dy in deltas:
                word = "".join(data.get((i + k * dx, j + k * dy), "") for k in range(4))
                ans += word == "XMAS" or word == "SAMX"

    return ans


def part2():
    ans = 0
    deltas = [(-1, -1), (1, -1), (1, 1), (-1, 1)]
    valid = ["SSMM", "MSSM", "MMSS", "SMMS"]

    for i, j in product(range(1, N - 1), range(1, M - 1)):
        if data[i, j] == "A":
            cross_letters = "".join(data[i + dx, j + dy] for dx, dy in deltas)
            ans += cross_letters in valid

    return ans


print(part1())
print(part2())
