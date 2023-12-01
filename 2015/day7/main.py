import parsing as p
from node import Node, find_node_by_name
import traversals as t


def main() -> None:
    nodes: list[Node] = []
    values: dict[str, int] = {}

    lines: list[str] = p.read_file("inputs.txt")
    for line in lines:
        nodes.append(Node(line))

    t.first_pass(nodes)
    t.valueCheck(nodes, values)

    completed: bool = False
    while not completed:
        t.check_and_execute(nodes, values)
        t.valueCheck(nodes, values)
        completed = t.check_for_completion(nodes, values)

    print(values["a"])


main()
