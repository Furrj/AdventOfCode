import parsing as p
from node import Node, find_node_by_name


def main() -> None:
    nodes: list[Node] = []
    lines: list[str] = p.read_file("test.txt")

    for line in lines:
        nodes.append(Node(line))

    for n in nodes:
        print(n)


main()
