from first import CPU


def solve(text: str):
    cpu = CPU()
    cpu.exec_all(text.splitlines())
    return cpu.max


if __name__ == "__main__":
    with open("input.txt") as file:
        print(solve(file.read()))
