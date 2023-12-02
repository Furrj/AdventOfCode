from parsing import read_file
from func import calc

FILENAME: str = "input.txt"

raw_lines = read_file(FILENAME)


if __name__ == "__main__":
    print(calc(raw_lines))
