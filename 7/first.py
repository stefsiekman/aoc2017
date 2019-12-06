from __future__ import annotations

from typing import Dict, List, Tuple


class Node:

    def __init__(self, name, weight):
        self.name: str = name
        self.weight: int = weight
        self.parent: Node = None
        self.children: List[Node] = []

    def root_parent(self):
        if self.parent is None:
            return self
        else:
            return self.parent.root_parent()

    def full_weight(self) -> int:
        return self.weight + sum(c.weight for c in self.children)

    def balanced(self) -> bool:
        return len(set(c.full_weight() for c in self.children)) <= 1

    def is_leaf(self) -> bool:
        return len(self.children) == 0

    def last_unbalanced(self) -> Node:
        return self

    def __str__(self):
        string = f"Node({self.name})"
        if not self.is_leaf():
            string += " -> "
            string += ', '.join(str(c.full_weight()) for c in self.children)
        return string

    def pprint(self, dont_shorten=False, indent=0):
        pre = '\t' * indent
        print(f"{pre}{self.name} {self.weight} ({self.full_weight()})")

        if not dont_shorten:
            if self.balanced():
                pre_extra = '\t' * (indent + 1)
                print(f"{pre_extra}...")
        else:
            for child in self.children:
                child.pprint(dont_shorten, indent + 1)

    def find(self, name) -> Node:
        if self.name == name:
            return self

        if self.is_leaf():
            return None

        for child in self.children:
            node = child.find(name)
            if node is not None:
                return node

    def adjust_target(self) -> Node:
        if self.parent is None \
                or self.parent.balanced() \
                or not self.balanced():
            for child in self.children:
                node = child.adjust_target()
                if node is not None:
                    return node
        else:
            return self

    def size(self) -> int:
        return 1 + sum(c.size() for c in self.children)


def create_tree(lines: List[str]) -> Node:
    nodes: Dict[str, Node] = dict()
    children: List[Tuple[Node, List[str]]] = list()

    print(f"Total of {len(lines)} lines to read.")

    for line in lines:
        parts = line.split(" -> ")
        weight = int(parts[0].split('(')[1][:-1])
        name = parts[0].split(' ')[0]

        node = Node(name, weight)
        nodes[name] = node
        if len(parts) > 1:
            children.append((node, parts[1].split(', ')))

    for node, childNames in children:
        for childName in childNames:
            assert childName in nodes
            node.children.append(nodes[childName])
            nodes[childName].parent = node

    root = nodes.popitem()[1].root_parent()
    print(f"Created tree with {root.size()} nodes.")

    return root


def solve(input: str):
    return create_tree(input.splitlines()).name


if __name__ == "__main__":
    with open("input.txt") as file:
        print(solve(file.read()))
