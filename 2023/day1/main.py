from parsing import read_file
from pathlib import Path


FILENAME: str = Path(__file__).parent / "input.txt"

raw_lines = read_file(FILENAME)


if __name__ == "__main__":
    for line in raw_lines:
        print(line)
