data = open(0).read().strip()
disk1 = [(i // 2 if i % 2 == 0 else -1, int(v)) for i, v in enumerate(data)]
disk2 = disk1.copy()


def checksum(disk):
    ans = 0
    k = 0
    for fileid, filelen in disk:
        if fileid != -1:
            ans += fileid * (filelen * k + (filelen) * (filelen - 1) // 2)
        k += filelen

    return ans


def part1():
    global disk1
    freeindex = 0

    while True:
        fileid, filelen = disk1[-1]
        fileindex = len(disk1) - 1
        if fileid == -1 or filelen == 0:
            disk1 = disk1[:-1]
            continue

        for _ in range(filelen):
            freeindex, freelen = next(
                (
                    (i + freeindex, flen)
                    for i, (fid, flen) in enumerate(disk1[freeindex:])
                    if fid == -1 and flen >= 1
                ),
                (None, None),
            )

            if freeindex is None or fileindex < freeindex:
                return checksum(disk1)

            disk1[fileindex] = (-1, 1)
            disk1[freeindex] = (-1, freelen - 1)
            disk1.insert(freeindex, (fileid, 1))
            fileindex += 1


def part2():
    global disk2

    for fileindex in reversed(range(len(disk2))):
        fileid, filelen = disk2[fileindex]
        if fileid == -1 or filelen == 0:
            continue

        freeindex, freelen = next(
            (
                (i, flen)
                for i, (fid, flen) in enumerate(disk2)
                if fid == -1 and flen >= filelen
            ),
            (None, None),
        )

        if freeindex is None or fileindex < freeindex:
            continue

        disk2[fileindex] = (-1, filelen)
        disk2[freeindex] = (-1, freelen - filelen)
        disk2.insert(freeindex, (fileid, filelen))

    return checksum(disk2)


print(part1())
print(part2())
