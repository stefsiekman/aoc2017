def solve(lines):
    instr = [int(i) for i in lines]

    steps = 0
    ptr = 0

    while True:
        steps += 1

        offs = instr[ptr]
        instr[ptr] += 1
        ptr += offs

        if ptr >= len(instr) or ptr < 0:
            break

    print(steps)


with open("input.txt", "r") as file:
    solve(file.read().splitlines())
