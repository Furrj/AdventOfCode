def read_file(filename: str) -> list[str]:
    lines: list[str] = []
    f = open(filename)

    for line in f:
        lines.append(line.strip())

    f.close()
    return lines
