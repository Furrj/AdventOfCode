from parsing import read_file
from Deer import Deer

T: str = "inputs/test.txt"
M: str = "inputs/main.txt"


if __name__ == "__main__":
    all_deer: list[Deer] = []
    for line in read_file(M):
        all_deer.append(Deer(line))

    for i in range(2503):
        distances = []

        for d in all_deer:
            d.turn()
            distances.append(d.distance)

        for d in all_deer:
            if d.distance == max(distances):
                d.addPoint()

    for d in all_deer:
        print(d)
