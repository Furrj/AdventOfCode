import parsing as p
import calculations as c


def main() -> None:
    lines: list[str] = p.read_file("inputs/input.txt")
    cities: list[str] = p.get_cities(lines)
    distances: list[tuple[str, str, int]] = p.get_distances(lines)

    routes = c.generate_perms(cities=cities)
    valid_routes = c.valid_routes(distances, routes)
    # for v in valid_routes:
    #     print(v)


main()
