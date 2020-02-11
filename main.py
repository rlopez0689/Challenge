from mars_rover.plateau import Plateau
from mars_rover.rover import Rover

ix, iy = input("Enter width and height of plateau").split()
plateau = Plateau(ix, iy)

end = False

while not end:
    rover_input = input("Enter x, y and direction of rover or Q to quit").split()
    if "Q" in rover_input:
        end = True
        print("Goodbye!")
    elif len(rover_input) == 3:
        rover = Rover(rover_input[0], rover_input[1], rover_input[2])
        plateau.send_rover(rover)

        for movement in input("Enter movements"):
            plateau.send_command(movement.upper())
        print(rover.x)
        print(rover.y)
        print(rover.get_direction())
    else:
        print("wrong format")