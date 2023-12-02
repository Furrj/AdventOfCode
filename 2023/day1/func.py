from collections import deque


def calc(lines: list[str]) -> int:
    total: int = 0

    for line in lines:
        total += _get_num(line)

    return total


def _get_num(line: str) -> int:
    res: str = ""

    for c in line:
        if c.isnumeric():
            res += c
            break

    for c in reversed(line):
        if c.isnumeric():
            res += c
            break

    return int(res)
