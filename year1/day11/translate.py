import validation as v


def increment(input: str) -> str:
    split = [x for x in input]

    for i in reversed(range(len(split))):
        if ord(split[i]) < ord("z"):
            split[i] = chr(ord(split[i]) + 1)
            break
        else:
            split[i] = "a"
            split[i - 1] = chr(ord(split[i - 1]) + 1)
            break

    return ("").join(split)


def find_valid(input: str) -> str:
    curr_str: str = input

    while True:
        curr_str = increment(curr_str)

        if (
            v.has_straight(curr_str)
            and not v.has_iol(curr_str)
            and v.has_doubles(curr_str)
        ):
            break

    return curr_str
