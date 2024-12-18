data = open(0).read().splitlines()
inp = [(*map(int, line.split(",")),) for line in data]

grid = {v: i for i, v in enumerate(inp)}
m = max(max(x, y) for x, y in inp)

start = (0, 0)
end = (m, m)


def bfs(tl):
    q = [(start, 0)]
    visited = set()

    while q:
        (x, y), d = q.pop(0)

        if (x, y) == end:
            return d

        if (x, y) in visited:
            continue
        visited.add((x, y))

        for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
            nx, ny = x + dx, y + dy

            if 0 <= nx <= m and 0 <= ny <= m and grid.get((nx, ny), tl) >= tl:
                q.append(((nx, ny), d + 1))


def part1():
    return bfs(1024 if m == 70 else 12)


def part2():
    lo, hi = 0, len(data)
    while lo < hi:
        if bfs(mid := (lo + hi) // 2):
            lo = mid + 1
        else:
            hi = mid

    return data[lo - 1]


print(part1())
print(part2())
