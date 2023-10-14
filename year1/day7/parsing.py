def readFile(filename: str) -> list[str]:
    lines: list[str] = []
    f = open(filename)
    for line in f:
        lines.append(line)
    return lines
