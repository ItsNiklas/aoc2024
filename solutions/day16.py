from collections import defaultdict

data = open(0).read().splitlines()

maze = {}
for y, line in enumerate(data):
    for x, c in enumerate(line):
        if c == "S":
            start = (x, y)
        if c == "E":
            end = (x, y)
        maze[x, y] = c


def bfs():
    q = [([(start[0] - 1, start[1])], start, 0)]
    dist = defaultdict(lambda: float("inf"))
    paths = defaultdict(set)

    while q:
        hist, (x, y), d = q.pop(0)
        (px, py) = hist[-1]

        if (x, y) == end:
            paths[d].update(hist)

        for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
            nx, ny = x + dx, y + dy

            if (nx, ny) == (px, py):
                continue

            newd = d + (1 if (x - px == dx) and (y - py == dy) else 1001)

            if maze[nx, ny] != "#" and newd < dist[nx, ny] + 1001:
                dist[nx, ny] = min(newd, dist[nx, ny])
                q.append((hist + [(x, y)], (nx, ny), newd))

    return dist, paths


dist, paths = bfs()


def part1():
    return dist[end]


def part2():
    return len(paths[dist[end]])


print(part1())
print(part2())
