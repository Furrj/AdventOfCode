from parsing import read_file

FILENAME: str = "input.txt"

raw_lines = read_file(FILENAME)


if __name__ == "__main__":
    a = "adc"
    b = "fdfdabcdfdf"

    print(b.find(a))
