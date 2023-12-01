import parsing as p


def translate(into: list[tuple[str, int]]) -> str:
    out: str = ""

    for t in into:
        if t[1] == 1:
            out += "1"
            out += t[0]
        else:
            out += str(t[1])
            out += t[0]

    return out


if __name__ == "__main__":
    curr_list: list[tuple[str, int]] = []
    answer: str = "1321131112"
    for i in range(50):
        curr_list = p.get_frequency(answer)
        answer = translate(curr_list)
    print(len(answer))
