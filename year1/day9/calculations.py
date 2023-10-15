from parsing import format_route


def generate_perms(
    cities: list[str], route: list[str] = [], routes: list[list[str]] = []
) -> list[list[str]]:
    if len(cities) == 0:
        routes.append(route.copy())

    for city in cities:
        route.append(city)
        choices: list[str] = cities.copy()
        choices.remove(city)
        generate_perms(cities=choices, route=route, routes=routes)
        route.pop()

    return routes


def validate_routes(
    routes: list[list[str]], distances: list[tuple[str, str, int]]
) -> list[list[str]]:
    valid_routes: list[list[str]] = []
    for r in routes:
        if validate_route(r, distances):
            valid_routes.append(r)

    return valid_routes


def validate_route(route: list[str], distances: list[tuple[str, str, int]]) -> bool:
    valid: bool = False
    for i in range(len(route) - 1):
        for d in distances:
            if route[i] in d and route[i + 1] in d:
                valid = True
                break
    return valid


def calculate_distances(
    routes: list[list[str]], distances: list[tuple[str, str, int]]
) -> list[tuple[str, int]]:
    calculated: list[tuple[str, int]] = []
    for r in routes:
        combined: tuple[str, int] = (format_route(r), calculate_distance(r, distances))
        calculated.append(combined)
    return calculated


def calculate_distance(route: list[str], distances: list[tuple[str, str, int]]) -> int:
    total: int = 0
    for i in range(len(route) - 1):
        for d in distances:
            if route[i] in d and route[i + 1] in d:
                total += d[2]
                break
    return total


def getMin(calculated: list[tuple[str, int]]) -> int:
    min: int = calculated[0][1]
    for c in calculated:
        if c[1] < min:
            min = c[1]
    return min


def getMax(calculated: list[tuple[str, int]]) -> int:
    min: int = calculated[0][1]
    for c in calculated:
        if c[1] > min:
            min = c[1]
    return min
