ENGLISH: dict[str, str] = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def calc(lines: list[str]) -> int:
    total: int = 0

    for line in lines:
        total += int(("").join(_get_nums(_get_min_max(line))))

    return total

def _get_nums(k: dict[str, str]) -> list[str]:
    out: list[str] = []

    for i in k.keys():
        if i.isnumeric():
            out.append(i)
        else:
            out.append(ENGLISH[i])

    if len(out) == 1:
        out.append(out[0])

    return out


def _get_min_max(line: str) -> dict[str, str]:
    pairs: list[tuple[str, str]] = _parse_nums(line)
    pairs = _parse_words(line, pairs)

    indexes = [int(x[1]) for x in pairs]

    min_max = ((str(min(indexes))), str(max(indexes)))
    out: dict[str, str] = {}

    for i in min_max:
        for p in pairs:
            if p[1] == i:
                out[p[0]] = p[1]

    return out

def _parse_nums(line: str, d: list[tuple[str, str]] = []) -> list[tuple[str, str]]:
    out = d.copy()

    for i, v in enumerate(line):
        if v.isnumeric():
            out.append((v, str(i)))
            break

    for i, v in enumerate(reversed(line)):
        if v.isnumeric():
            out.append((v, str(len(line) - (i+1))))
            break

    return out

def _parse_words(line: str, d: list[tuple[str, str]] = []) -> list[tuple[str, str]]:
    out = d.copy()

    def recurse(line: str, s: str, index: int = 0):
        nonlocal out

        i = line.find(s)
        if i != -1:
            out.append((s, str(i + index)))
            j = i + (len(s))
            recurse(line[j:], s,  j+index)
        else:
            return

    for i in ENGLISH:
        recurse(line, i)


    return out