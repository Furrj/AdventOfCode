def has_straight(input: str) -> bool:
    split = [x for x in input]

    for i in range(len(split) - 2):
        if ord(split[i + 1]) == (ord(split[i]) + 1) and ord(split[i + 2]) == (
            ord(split[i]) + 2
        ):
            return True

    return False


def has_iol(input: str) -> bool:
    if "i" in input:
        return True
    if "o" in input:
        return True
    if "l" in input:
        return True

    return False


def has_doubles(input: str) -> bool:
    split = [x for x in input]
    first_match = ""
    count = 0

    for i in range(len(input) - 1):
        if input[i] == input[i + 1]:
            count += 1
            first_match += input[i]
            break

    for i in range(len(input) - 1):
        if input[i] == input[i + 1] and input[i] not in first_match:
            count += 1
            break

    if count >= 2:
        return True
    else:
        return False
