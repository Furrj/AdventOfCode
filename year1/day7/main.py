import parsing as p
from node import Node


def main() -> None:
    nodes: list[Node] = []
    lines: list[str] = p.read_file("test.txt")

    for line in lines:
        nodes.append(Node(line))

    for node in nodes:
        print(node)


main()
