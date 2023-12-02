ENGLISH: dict[str, int] = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def calc(lines: list[str]) -> int:
    total: int = 0

    for line in lines:
        total += _get_num(line)

    return total


def _get_num(line: str) -> int:
    matches: 
