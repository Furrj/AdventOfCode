import parsing as p
import calculations as c


def main() -> None:
    lines: list[str] = p.read_file("inputs/input.txt")
    cities: list[str] = p.get_cities(lines)
    routes_and_distances: list[tuple[str, str, int]] = p.get_distances(lines)

    route_perms = c.generate_perms(cities=cities)
    valid_routes = c.validate_routes(route_perms, routes_and_distances)

    calculated_routes = c.calculate_distances(valid_routes, routes_and_distances)
    print(c.getMin(calculated_routes))


main()
