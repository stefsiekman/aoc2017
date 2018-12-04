def solve(digits):
    sum = 0
    for i in range(0, len(digits)):
        this = digits[i]
        nextIndex = i + int(len(digits)/2)
        next = digits[nextIndex % len(digits)]

        if this == next:
            sum += int(this)

    print(sum)


with open("input.txt", "r") as file:
    solve(file.read().splitlines()[0])
