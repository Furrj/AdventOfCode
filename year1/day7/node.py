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
        self.name = p.get_name(line)
        self.instruction = p.get_instruction(line)
        self.instruction_type = p.get_instruction_type(self.instruction)
        self.operation = p.get_operation(self.instruction)

    def __str__(self):
        string: str = "{\n"
        string += f"  Name: {self.name}\n"
        string += f"  Instruction: {self.instruction}\n"
        string += f"  InstructionType: {self.instruction_type.name}\n"
        string += f"  Operation: {self.operation.name}\n"
        string += "}\n"
        return string
