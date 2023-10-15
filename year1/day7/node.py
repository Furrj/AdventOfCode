from enum import Enum
import parsing as p


class Operations(Enum):
    AND = 1
    OR = 2
    NOT = 3
    LSHIFT = 4
    RSHIFT = 5
    NONE = 6


class InstructionTypes(Enum):
    DIRECT_NUMBER = 1
    DIRECT_PARENT = 2
    UNARY = 3
    L_PARENT = 4
    R_PARENT = 5
    BINARY = 6


class Node:
    name: str
    instruction: str
    instruction_type: InstructionTypes
    instruction_list: list[str]
    operation: Operations
    operands: list[str]
    value: int
    parents: list[str]

    def __init__(self, line: str):
        if line == "null":
            return

        self.name = p.get_name(line)
        self.instruction = p.get_instruction(line)
        self.instruction_list = self.instruction.split(" ")
        self.instruction_type = p.get_instruction_type(self.instruction_list)
        self.operation = p.get_operation(self.instruction)
        self.operands = p.get_operands(self.instruction_list, self.instruction_type)
        self.parents = p.get_parents(self.instruction_list, self.instruction_type)
        self.value = -1

    def __str__(self):
        string: str = "{\n"
        string += f"  Name: {self.name}\n"
        string += f"  Instruction: {self.instruction}\n"
        string += f"  Instruction_type: {self.instruction_type.name}\n"
        string += f"  Operation: {self.operation.name}\n"
        string += f"  Operands: {self.operands}\n"
        string += f"  Parents: {self.parents}\n"
        string += f"  Value: {self.value}\n"
        string += "}\n"
        return string


def find_node_by_name(searchName: str, nodes: list[Node]) -> tuple[Node, bool]:
    for n in nodes:
        if n.name == searchName:
            return n, True
    return Node("null"), False
