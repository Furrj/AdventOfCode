from node import Node, InstructionTypes
from exec import exec_instructions


def valueCheck(nodes: list[Node], values: dict[str, int]) -> None:
    for node in nodes:
        if node.value != -1:
            if node.name not in values.keys():
                values[node.name] = node.value


def first_pass(nodes: list[Node]) -> None:
    for node in nodes:
        if node.instruction_type == InstructionTypes.DIRECT_NUMBER:
            node.value = int(node.instruction)


def check_and_execute(nodes: list[Node], values: dict[str, int]) -> None:
    for node in nodes:
        if node.name in values.keys():
            continue
        parentsHaveValues: bool = True
        for parent in node.parents:
            if parent not in values.keys():
                parentsHaveValues = False
        if parentsHaveValues:
            exec_instructions(node, values)
