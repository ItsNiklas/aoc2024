data = open(0).read().splitlines()
inp = {(j, i): c for i, l in enumerate(data) for j, c in enumerate(l)}


def bfs(start):
    q = [start]
    area = set()
    per = list()

    while q:
        x, y = q.pop(0)
        if (x, y) in area:
            continue
        area.add((x, y))

        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            if (nx := x + dx, ny := y + dy) not in area:
                if (nx, ny) in inp and inp[(nx, ny)] == inp[start]:
                    q.append((nx, ny))
                else:
                    per.append((x, y, nx, ny))

    return area, per


def part1():
    ans = 0
    visited = set()

    for x, y in inp:
        if (x, y) in visited:
            continue

        area, per = bfs((x, y))
        visited |= area
        ans += len(per) * len(area)

    return ans


def part2():
    ans = 0
    visited = set()

    for x, y in inp:
        if (x, y) in visited:
            continue

        area, per = bfs((x, y))
        visited |= area

        sides = {
            (oi, oj, i, j)  # We add one element per side by skipping ones below/right
            for oi, oj, i, j in per  # To double-count inner corners, we need the origin
            if (oi + 1, oj, i + 1, j) not in per and (oi, oj + 1, i, j + 1) not in per
        }

        ans += len(sides) * len(area)

    return ans


print(part1())
print(part2())
