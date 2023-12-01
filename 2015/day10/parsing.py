def get_frequency(into: str) -> list[tuple[str, int]]:
    diffs: list[tuple[str, int]] = []
    curr: str = into[0]
    count = 0

    for i in range(len(into)):
        if i < len(into) - 1:
            if into[i] == curr:
                count += 1
            else:
                diffs.append((curr, count))
                count = 1
                curr = into[i]
        else:
            if into[i] == curr:
                count += 1
                diffs.append((curr, count))
            else:
                diffs.append((curr, count))
                diffs.append((into[i], 1))

    return diffs
