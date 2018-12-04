def solve(lines):
    sum  = 0
    for line in lines:
        nums = [int(n) for n in line.split("\t")]

        sets = [(a,b) for a in nums for b in nums if a != b]

        for (a,b) in sets:
            if a / b % 1.0 == 0:
                sum += int(a / b)
                break

    print(sum)

with open("input.txt", "r") as file:
    solve(file.read().splitlines())
