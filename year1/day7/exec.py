from node import Node, find_node_by_name, InstructionTypes, Operations


def exec_instructions(node: Node, values: dict[str, int]) -> None:
    if node.instruction_type == InstructionTypes.DIRECT_PARENT:
        node.value = values[node.parents[0]]
    if node.instruction_type == InstructionTypes.L_PARENT:
        operands: list[int] = []
        operands[0] = values[node.parents[0]]
