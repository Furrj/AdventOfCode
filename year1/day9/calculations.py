def calculate_distances(
    cities: list[str], distances: list[tuple[str, str, int]], routes: list[list[str]]
) -> list[tuple[str, int]]:
    route_distances: list[tuple[str, int]] = []

    return route_distances


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


def valid_routes(
    distances: list[tuple[str, str, int]], routes: list[list[str]]
) -> list[list[str]]:
    valid_routes: list[list[str]] = []

    for route in routes:
        for i in range(len(route) - 1):
            valid: bool = False
            for d in distances:
                if route[i] in distances and route[i + 1] in distances:
                    valid = True

    return valid_routes
