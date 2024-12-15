from itertools import count

data = open(0).read().split("\n\n")
grid = data[0].splitlines()
moves = data[1].replace("\n", "")

deltas = {"<": (-1, 0), ">": (1, 0), "^": (0, -1), "v": (0, 1)}


def part1():
    wh = {}
    for y, line in enumerate(grid):
        for x, c in enumerate(line):
            if c == "@":
                curr = (x, y)
                wh[x, y] = "."
            else:
                wh[x, y] = c

    for move in moves:
        dx, dy = deltas[move]
        x, y = curr
        nx, ny = x + dx, y + dy

        if (k := next(k for k in count(1) if wh[x + k * dx, y + k * dy] != "O")) > 1:
            if wh[after := (x + k * dx, y + k * dy)] == "#":
                continue

            wh[nx, ny], wh[after] = wh[after], wh[nx, ny]  # Push all (Swap)

        curr = (nx, ny) if wh[nx, ny] == "." else curr

    return sum(x + 100 * y for x, y in wh if wh[x, y] == "O")


def part2():
    wh = {}
    for y, line in enumerate(grid):
        for x, c in enumerate(line):
            if c == "@":
                curr = (x * 2, y)
                wh[x * 2, y], wh[x * 2 + 1, y] = ".."
            elif c == "#":
                wh[x * 2, y], wh[x * 2 + 1, y] = "##"
            elif c == ".":
                wh[x * 2, y], wh[x * 2 + 1, y] = ".."
            elif c == "O":
                wh[x * 2, y], wh[x * 2 + 1, y] = "[]"

    for move in moves:
        dx, dy = deltas[move]
        x, y = curr
        nx, ny = x + dx, y + dy

        if wh[nx, ny] == "#":
            continue

        if wh[nx, ny] == ".":
            curr = nx, ny
            continue

        if move == "<" or move == ">":  # Push horizontal like in Part 1
            if (k := next(k for k in count(1) if wh[x + k * dx, y] not in "[]")) > 1:
                if wh[x + k * dx, y] == "#":
                    continue

                wh[nx, ny] = "."
                for i in range(2, k + 1):
                    wh[x + i * dx, y] = "[" if (i % 2) ^ (move == ">") else "]"
                curr = (nx, ny)

        else:  # Build dependency graph for pushable boxes vertically
            boxes = set()

            def pushable(lx, rx, by):
                lpos, rpos = (lx, by),(rx, by)
                by += dy
                vert = wh[lx, by] + wh[rx, by]

                if vert == "..":  # ..
                    boxes.add((lpos, rpos))
                    return True
                if vert == ".[":  # .[
                    if pushable(rx, rx + 1, by):
                        boxes.add((lpos, rpos))
                        return True
                if vert == "].":  # ].
                    if pushable(lx - 1, lx, by):
                        boxes.add((lpos, rpos))
                        return True
                if vert == "[]":  # []
                    if pushable(lx, rx, by):
                        boxes.add((lpos, rpos))
                        return True
                elif vert == "][":  # ][
                    if pushable(lx - 1, lx, by) and pushable(rx, rx + 1, by):
                        boxes.add((lpos, rpos))
                        return True

            if pushable(nx - (wh[nx, ny] == "]"), nx + (wh[nx, ny] == "["), ny):
                for lpos, rpos in boxes:
                    wh[lpos], wh[rpos] = ".", "."
                    wh[lpos[0], lpos[1] + dy], wh[rpos[0], rpos[1] + dy] = "[", "]"
                curr = (nx, ny)

    return sum(x + 100 * y for x, y in wh if wh[x, y] == "[")


print(part1())
print(part2())
