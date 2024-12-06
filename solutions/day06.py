data = open(0).readlines()
grid = {(j, i): c for i, r in enumerate(data) for j, c in enumerate(r.strip())}
start = next(p for p in grid if grid[p] == "^")

dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]


def walk(grid):
    history = set()  # We have to keep this, but it is the main bottleneck
    d, x, y = 0, *start

    while True:
        history.add((x, y, d))
        dx, dy = dirs[d]  # Unfortunately, complex numbers were 3x slower than tuples

        if not 0 <= x + dx < len(data) or not 0 <= y + dy < len(data[0]) - 1:  # OoB
            return history
        elif grid[(x + dx, y + dy)] == "#":  # Wall, turn right
            d = (d + 1) % 4
        else:
            x += dx
            y += dy
            if (x, y, d) in history:  # Loop detected (slow)
                return None


def part1():
    return len({(x, y) for x, y, _ in walk(grid)})


def part2():
    return sum(
        walk(grid | {new: "#"}) is None for new in {(x, y) for x, y, _ in walk(grid)}
    )


print(part1())
print(part2())
