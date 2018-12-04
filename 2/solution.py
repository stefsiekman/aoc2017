def solve(lines):
    sum  = 0
    for line in lines:
        nums = [int(n) for n in line.split("\t")]
        sum += max(nums) - min(nums)
    print(sum)

with open("input.txt", "r") as file:
    solve(file.read().splitlines())
