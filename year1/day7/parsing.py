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


def get_instruction_type(instruction: str) -> InstructionTypes:
    splitInstructions: list = instruction.split(" ")
    if len(splitInstructions) == 1:
        if splitInstructions[0].isnumeric():
            return InstructionTypes.DIRECT_NUMBER
        else:
            return InstructionTypes.DIRECT_PARENT

    if len(splitInstructions) == 2:
        return InstructionTypes.UNARY

    if splitInstructions[0].isnumeric() and splitInstructions[2].isalpha():
        return InstructionTypes.R_PARENT

    if splitInstructions[0].isalpha() and splitInstructions[2].isnumeric():
        return InstructionTypes.L_PARENT

    return InstructionTypes.BINARY


def get_operation(instruction: str) -> Operations:
    for o in Operations:
        if o.name in instruction:
            return o
    return Operations.NONE


def get_parents(instruction: str, instruction_type: InstructionTypes) -> list[str]:
    parents: list[str] = []
    splitInstructions: list = instruction.split(" ")

    if instruction_type == InstructionTypes.DIRECT_NUMBER:
        parents.append("none")
    elif instruction_type == InstructionTypes.DIRECT_PARENT:
        parents.append(splitInstructions[0])
    elif instruction_type == InstructionTypes.L_PARENT:
        parents.append(splitInstructions[0])
    elif instruction_type == InstructionTypes.R_PARENT:
        parents.append(splitInstructions[2])
    elif instruction_type == InstructionTypes.UNARY:
        parents.append(splitInstructions[1])
    elif instruction_type == InstructionTypes.BINARY:
        parents.append(splitInstructions[0])
        parents.append(splitInstructions[2])

    return parents
