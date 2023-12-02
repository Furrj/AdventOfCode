from parsing import read_file
import func as f
import re

FILENAME: str = "input.txt"
TEST: str = "test.txt"

raw_lines: list[str] = read_file(FILENAME)

if __name__ == "__main__":
    all = f.calc(raw_lines)
    print(all)