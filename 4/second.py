from itertools import permutations

def solve(lines):
    valids = 0
    for line in lines:
        words = line.split(" ")

        valid = True
        for i in range(0, len(words)):
            if not valid:
                break
            for j in range(i + 1, len(words)):
                if not valid:
                    break
                if words[i] in ["".join(a) for a in list(permutations(words[j]))]:
                    valid = False

        if valid:
            valids += 1

    print(valids)


with open("input.txt", "r") as file:
    solve(file.read().splitlines())
