from pathlib import Path


def read_file(filename: str) -> list[str]:
    lines: list[str] = []
    f = open(Path(__file__).parent / filename)

    for line in f:
        lines.append(line)

    f.close()
    return lines
