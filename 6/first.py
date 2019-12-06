import itertools


def distribute(mem):
    new_mem = mem[:]
    index = new_mem.index(max(new_mem))
    remaining = new_mem[index]
    new_mem[index] = 0
    for _ in range(remaining):
        index += 1
        new_mem[index % len(new_mem)] += 1
    return new_mem


if __name__ == "__main__":
    with open("input.txt") as file:
        memory = list(itertools.chain(*[line.split('\t')
                                        for line in file.readlines()]))
        memory = [int(m) for m in memory]

        seen = set(memory)
        needed = 0

        while True:
            string = '\t'.join([str(m) for m in memory])
            if string in seen:
                break

            memory = distribute(memory)
            needed += 1
            seen.add(string)

        print(needed)

