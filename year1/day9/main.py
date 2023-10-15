import parsing as p
import calculations as c


def main() -> None:
    lines: list[str] = p.read_file("inputs/test_input.txt")
    cities: list[str] = p.get_cities(lines)
    distances: list[tuple[str, str, int]] = p.get_distances(lines)

    routes = c.calculate_routes(cities, distances)
    print(distances)


main()
