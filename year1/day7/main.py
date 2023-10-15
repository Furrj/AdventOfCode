import parsing as p
from node import Node, find_node_by_name
import traversals as t


def main() -> None:
    nodes: list[Node] = []
    values: dict[str, int] = {}

    lines: list[str] = p.read_file("inputs.txt")
    for line in lines:
        nodes.append(Node(line))

    for node in nodes:
        print(node)


main()
