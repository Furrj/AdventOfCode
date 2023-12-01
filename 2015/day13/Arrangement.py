class Arrangement:
    person: str
    amount: int
    neighbor: str

    def __init__(self, line: str) -> None:
        split: list[str] = line.split(" ")
        self.person = split[0]
        self.amount = int(split[3])
        if split[2] == "lose":
            self.amount *= -1
        self.neighbor = split[10].strip()[:-1]

    def __str__(self):
        return f"{self.person} -> {self.neighbor}: {self.amount}"
