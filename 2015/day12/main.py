import json

f = open("input.json")

data = json.loads(f.read())

f.close()


def parse_dict(data: any):
    total = 0

    if isinstance(data, dict):
        for v in data.values():
            if "red" in data.values():
                return 0
            # if isinstance(v, dict) and "red" in v.values():
            #     continue
            # else:
            total += parse_dict(v)
    if isinstance(data, list):
        for v in data:
            # if isinstance(v, dict) and "red" in v.values():
            #     continue
            # else:
            total += parse_dict(v)
    if isinstance(data, int):
        total += data

    return total


print(parse_dict(data))
