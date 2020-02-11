
class Plateau:
    rover = None

    def __init__(self, width, height):
        self.width = int(width)
        self.height = int(height)

    def send_rover(self, rover):
        self.rover = rover

    def send_command(self, movement):
        if movement == "M":
            self.rover.move()
        elif movement == "L" or movement == "R":
            self.rover.change_direction(movement)
