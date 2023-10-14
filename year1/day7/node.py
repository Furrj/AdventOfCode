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
    operation: Operations
    value: int
    parents: list[str]

    def __init__(self, line: str):
        if line == "null":
            return

        self.name = p.get_name(line)
        self.instruction = p.get_instruction(line)
        self.instruction_type = p.get_instruction_type(self.instruction)
        self.operation = p.get_operation(self.instruction)
        self.parents = p.get_parents(self.instruction, self.instruction_type)

    def __str__(self):
        string: str = "{\n"
        string += f"  Name: {self.name}\n"
        string += f"  Instruction: {self.instruction}\n"
        string += f"  InstructionType: {self.instruction_type.name}\n"
        string += f"  Operation: {self.operation.name}\n"
        string += f"  Parents: {self.parents}\n"
        string += "}\n"
        return string


def find_node_by_name(searchName: str, nodes: list[Node]) -> tuple[Node, bool]:
    for n in nodes:
        if n.name == searchName:
            return n, True
    return Node("null"), False
