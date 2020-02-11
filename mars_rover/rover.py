class Rover:
    positions = ["N", "E", "S", "W"]

    def __init__(self, x, y, direction):
        self.x = int(x)
        self.y = int(y)
        self.direction = self.positions.index(direction.upper())

    def get_direction(self):
        return self.positions[self.direction]

    def move(self):
        if self.direction == 0:
            self.y += 1
        elif self.direction == 1:
            self.x += 1
        elif self.direction == 2:
            self.y -= 1
        elif self.direction == 3:
            self.x -= 1

    def change_direction(self, movement):
        if movement == "R":
            self.direction = 0 if (self.direction + 1) > 3 else (self.direction + 1)
        elif movement == "L":
            self.direction = 3 if (self.direction - 1) < 0 else (self.direction - 1)
