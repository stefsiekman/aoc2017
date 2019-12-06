from typing import List, Tuple, Dict


class CPU:

    def __init__(self):
        self.registers = dict()
        self.max = None

    def exec(self, line):
        inst = line.split(' if ')[0]
        cond = line.split(' if ')[1]

        inst = inst.replace("inc ", "+").replace("dec ", "-")
        op_register = inst.split(" ")[0]
        diff = eval(inst.split(" ")[1])

        cond_register = cond.split(" ")[0]
        cond = cond.replace(cond_register,
                            str(self.get_register(cond_register)))

        if eval(cond):
            self.add_register(op_register, diff)

    def add_register(self, name, diff):
        if name not in self.registers:
            self.registers[name] = 0

        self.registers[name] += diff

        if self.max is None or self.registers[name] > self.max:
            self.max = self.registers[name]

    def max_register(self):
        return max(self.registers.values())

    def get_register(self, name):
        return self.registers[name] if name in self.registers else 0

    def exec_all(self, lines: List[str]):
        for line in lines:
            self.exec(line)


def solve(text: str):
    cpu = CPU()
    cpu.exec_all(text.splitlines())
    return cpu.max_register()


if __name__ == "__main__":
    with open("input.txt") as file:
        print(solve(file.read()))
