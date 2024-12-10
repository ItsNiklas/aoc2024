data = open(0).read().splitlines()
inp = [[*map(int, list(x))] for x in data]  # Complex numbers are slooow

trailheads = [
    (j, i) for i in range(len(inp)) for j in range(len(inp[i])) if inp[i][j] == 0
]


def bfs(start):
    stack = [(start, tuple())]  # Include the history in the state
    visited, peaks, paths = set(), set(), set()
    while stack:
        (x, y), hist = stack.pop()

        if ((x, y), hist) in visited:
            continue
        visited.add(((x, y), hist))

        if inp[y][x] == 9:  # We found a peak!
            peaks.add((x, y))  # Count the accessible peaks
            paths.add(hist + ((x, y),))  # Count the paths to the peaks
            continue

        stack.extend(
            ((nx, ny), hist + ((x, y),))  # Add new history to the state
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]
            if (
                0 <= (nx := x + dx) < len(inp[0])
                and 0 <= (ny := y + dy) < len(inp)
                and inp[ny][nx] == inp[y][x] + 1  # Only if the next step is valid (+1)
            )
        )

    return peaks, paths


def part1():
    return sum(len(bfs(head)[0]) for head in trailheads)


def part2():
    return sum(len(bfs(head)[1]) for head in trailheads)


print(part1())
print(part2())
