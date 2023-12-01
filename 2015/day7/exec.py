from node import Node, find_node_by_name, InstructionTypes, Operations


def exec_instructions(node: Node, values: dict[str, int]) -> None:
    operands: list[int] = []
    if node.instruction_type == InstructionTypes.DIRECT_PARENT:
        node.value = values[node.parents[0]]
        return
    elif node.instruction_type == InstructionTypes.UNARY:
        operand: int = values[node.operands[0]]
        node.value = 65535 - operand
        return
    elif node.instruction_type == InstructionTypes.L_PARENT:
        operands.append(values[node.operands[0]])
        operands.append(int(node.operands[1]))
    elif node.instruction_type == InstructionTypes.R_PARENT:
        operands.append(int(node.operands[0]))
        operands.append(values[node.operands[1]])
    elif node.instruction_type == InstructionTypes.BINARY:
        operands.append(values[node.operands[0]])
        operands.append(values[node.operands[1]])
    node.value = exec_operation(node.operation, operands)


def exec_operation(operation: Operations, operands: list[int]) -> int:
    if operation == Operations.AND:
        return operands[0] & operands[1]
    if operation == Operations.OR:
        return operands[0] | operands[1]
    if operation == Operations.LSHIFT:
        return operands[0] << operands[1]
    if operation == Operations.RSHIFT:
        return operands[0] >> operands[1]
    return -1
