def read_file(filename: str) -> list[str]:
    lines: list[str] = []
    f = open(filename)

    for line in f:
        lines.append(line)

    f.close()

    return lines


def get_cities(lines: list[str]) -> list[str]:
    names: list[str] = []
    for l in lines:
        split: list[str] = l.split(" ")
        cities: tuple[str, str] = (split[0], split[2])
        for c in cities:
            if c not in names:
                names.append(c)
    return names


def get_distances(lines: list[str]) -> list[tuple[str, str, int]]:
    distances: list[tuple[str, str, int]] = []
    for l in lines:
        split: list[str] = l.split(" ")
        distance: tuple[str, str, int] = (split[0], split[2], int(split[4]))
        distances.append(distance)
    return distances
