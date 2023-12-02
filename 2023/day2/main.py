from parsing import read_file


FILENAME: str = "input.txt"
TEST: str = "test.txt"

raw_lines: list[str] = read_file(TEST)

if __name__ == "__main__":
    print(raw_lines)