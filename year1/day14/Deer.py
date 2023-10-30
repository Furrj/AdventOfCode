class Deer:
    name: str
    moving_time: int
    resting_time: int
    speed: int
    is_moving: bool
    time_left: int
    distance: int = 0
    points: int = 0

    def __init__(self, line: str):
        split = line.split(" ")
        self.name = split[0]
        self.speed = int(split[3])
        self.moving_time = int(split[6])
        self.resting_time = int(split[13])
        self.is_moving = True
        self.time_left = self.moving_time

    def toggle(self) -> None:
        if self.is_moving:
            self.time_left = self.resting_time
        else:
            self.time_left = self.moving_time
        self.is_moving = not self.is_moving

    def turn(self) -> None:
        if self.time_left == 0:
            self.toggle()

        if self.is_moving:
            self.distance += self.speed

        self.time_left -= 1

    def addPoint(self) -> None:
        self.points += 1

    def __str__(self) -> str:
        out: str = f"Name: {self.name}\n"
        out += f"Speed: {self.speed} for {self.moving_time} turns\n"
        out += f"Rest: {self.resting_time}\n"
        out += f"Distance: {self.distance}\n"
        out += f"Points: {self.points}\n"
        return out
