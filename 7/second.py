from first import create_tree, Node


def solve(input: str):
    root = create_tree(input.splitlines())
    root.adjust_target().pprint(True)
    target = root.adjust_target()
    sib_weights = set(c.full_weight() for c in target.parent.children)
    target_weight = (sib_weights - {target.full_weight()}).pop()

    goal_weight = target.weight - (target.full_weight() - target_weight)

    return goal_weight


if __name__ == "__main__":
    with open("input.txt") as file:
        print(solve(file.read()))
