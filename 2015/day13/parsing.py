def read_file(filename: str) -> list[str]:
    lines: list[str] = []
    f = open(filename)

    for line in f:
        lines.append(line)

    f.close()
    return lines
