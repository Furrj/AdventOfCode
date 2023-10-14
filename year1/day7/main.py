from parsing import readFile


def main() -> None:
    lines: list[str] = readFile("test.txt")
    for line in lines:
        print(line)


main()
