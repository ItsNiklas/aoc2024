data = open(0).read().splitlines()
grid = {(j, i): c for i, line in enumerate(data) for j, c in enumerate(line)}
start = next(k for k, v in grid.items() if v == "S")
end = next(k for k, v in grid.items() if v == "E")


def bfs():
    q = [(start, 0, None)]
    best = dict()

    while q:
        (x, y), t, prev = q.pop(0)

        if best.get((x, y), float("inf")) > t:
            best[(x, y)] = t

        for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
            nx, ny = x + dx, y + dy

            if (nx, ny) == prev:
                continue

            if grid.get((nx, ny)) != "#":
                q.append(((nx, ny), t + 1, (x, y)))

    return best


def ans(cheat_d):
    best = bfs()
    ans = 0

    for (x, y), curr_t in best.items():
        for dx in range(-cheat_d, cheat_d + 1):
            for dy in range(-cheat_d + abs(dx), cheat_d - abs(dx) + 1):
                nx, ny = x + dx, y + dy
                ans += best.get((nx, ny), 0) - curr_t - (abs(dx) + abs(dy)) >= 100

    return ans


def part1():
    return ans(2)


def part2():
    return ans(20)


print(part1())
print(part2())
