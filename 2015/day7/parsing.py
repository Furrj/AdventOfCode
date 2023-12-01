from node import Operations, InstructionTypes


def read_file(filename: str) -> list[str]:
    lines: list[str] = []
    f = open(filename)
    for line in f:
        lines.append(line)
    f.close()
    return lines


def get_instruction(line: str) -> str:
    instruction: str = ""
    for c in line:
        if c == "-":
            break
        else:
            instruction += c
    return instruction.strip()


def get_name(line: str) -> str:
    name: str = ""

    for i, c in enumerate(line):
        if c == ">":
            name = line[i + 2 :]
            break

    return name.strip()


def get_instruction_type(instruction_list: list[str]) -> InstructionTypes:
    if len(instruction_list) == 1:
        if instruction_list[0].isnumeric():
            return InstructionTypes.DIRECT_NUMBER
        else:
            return InstructionTypes.DIRECT_PARENT

    if len(instruction_list) == 2:
        return InstructionTypes.UNARY

    if instruction_list[0].isnumeric() and instruction_list[2].isalpha():
        return InstructionTypes.R_PARENT

    if instruction_list[0].isalpha() and instruction_list[2].isnumeric():
        return InstructionTypes.L_PARENT

    return InstructionTypes.BINARY


def get_operation(instruction: str) -> Operations:
    for o in Operations:
        if o.name in instruction:
            return o
    return Operations.NONE


def get_parents(
    instruction_list: list[str], instruction_type: InstructionTypes
) -> list[str]:
    parents: list[str] = []

    if instruction_type == InstructionTypes.DIRECT_NUMBER:
        parents.append("none")
    elif instruction_type == InstructionTypes.DIRECT_PARENT:
        parents.append(instruction_list[0])
    elif instruction_type == InstructionTypes.L_PARENT:
        parents.append(instruction_list[0])
    elif instruction_type == InstructionTypes.R_PARENT:
        parents.append(instruction_list[2])
    elif instruction_type == InstructionTypes.UNARY:
        parents.append(instruction_list[1])
    elif instruction_type == InstructionTypes.BINARY:
        parents.append(instruction_list[0])
        parents.append(instruction_list[2])

    return parents


def get_operands(
    instruction_list: list[str], instruction_type: InstructionTypes
) -> list[str]:
    operands: list[str] = []
    if (
        instruction_type == InstructionTypes.DIRECT_NUMBER
        or instruction_type == InstructionTypes.DIRECT_PARENT
    ):
        operands.append("none")
    elif instruction_type == InstructionTypes.UNARY:
        operands.append(instruction_list[1])
    else:
        operands.append(instruction_list[0])
        operands.append(instruction_list[2])
    return operands
