import itertools

from parsing import read_file
from Arrangement import Arrangement
from calculations import get_max

T: str = "inputs/test.txt"
M: str = "inputs/main.txt"


if __name__ == "__main__":
    arrs: list[Arrangement] = []
    people: list[str] = ["Me"]

    for l in read_file(M):
        arrs.append(Arrangement(l))

    for a in arrs:
        if a.person not in people:
            people.append(a.person)

    plans = list(itertools.permutations(people))

    print(get_max(plans, arrs))
