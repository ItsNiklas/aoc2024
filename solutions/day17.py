import re


data = open(0).read()
gA, _, _, *prog = list(map(int, re.findall(r"\d+", data)))


def run(A, B=0, C=0):  # This only works because every program has jnz(0) at the end!
    combo = lambda k: k if k <= 3 else [A, B, C][k - 4]
    ip = 0
    while ip < len(prog):
        match prog[ip]:
            case 0:  # adv
                A = A >> combo(prog[ip + 1])
            case 1:  # bxl
                B = B ^ prog[ip + 1]
            case 2:  # bst
                B = combo(prog[ip + 1]) % 8
            case 3:  # jnz
                if A:
                    ip = prog[ip + 1]
                    continue
            case 4:  # bxc
                B = B ^ C
            case 5:  # out
                return combo(prog[ip + 1]) % 8, A
            case 6:  # bdv
                B = A >> combo(prog[ip + 1])
            case 7:  # cdv
                C = A >> combo(prog[ip + 1])

        ip += 2


def part1():
    A = gA
    out = []

    while A:
        res, A = run(A)  # In practice, B and C are not needed due to program structure
        out.append(str(res))

    return ",".join(out)


def part2():
    st = [(0, 0)]  # run = lambda A: (A % 8) ^ 3 ^ (A >> ((A % 8) ^ 5)) % 8
    rp = [*reversed(prog)]
    results = []

    while st:
        k, res = st.pop()
        if k == len(rp):
            results.append(res)
            continue

        st.extend((k + 1, (res + A) << 3) for A in range(8) if run(res + A)[0] == rp[k])

    return min(results) >> 3


print(part1())
print(part2())
