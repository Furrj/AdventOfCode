def read_file(filename: str) -> list[str]:
    lines: list[str] = []
    f = open(filename)

    for line in f:
        lines.append(line.strip()[:-1])

    f.close()
    return lines
