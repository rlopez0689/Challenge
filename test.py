
import unittest
from mars_rover.plateau import Plateau
from mars_rover.rover import Rover


class TestMarsRovers(unittest.TestCase):

    def test_deployment(self):
        command_test_one = ["L", "M", "L", "M", "L", "M", "L", "M", "M"]
        command_test_two = ["M", "M", "R", "M", "M", "R", "M", "R", "R", "M"]
        self.plateau = Plateau(5, 5)

        rover_one = Rover("1", "2", "N")
        rover_two = Rover("3", "3", "E")

        self.plateau.send_rover(rover_one)
        for command in command_test_one:
            self.plateau.send_command(command)
        self.assertEqual("N", rover_one.get_direction())
        self.assertEqual(1, rover_one.x)
        self.assertEqual(3, rover_one.y)

        self.plateau.send_rover(rover_two)
        for command in command_test_two:
            self.plateau.send_command(command)
        self.assertEqual("E", rover_two.get_direction())
        self.assertEqual(5, rover_two.x)
        self.assertEqual(1, rover_two.y)

    def test_rover_movement(self):
        rover = Rover("1", "2", "N")
        rover.move()
        self.assertEqual(3, rover.y)
        self.assertEqual(1, rover.x)

        rover = Rover("1", "2", "E")
        rover.move()
        self.assertEqual(2, rover.y)
        self.assertEqual(2, rover.x)

        rover = Rover("1", "2", "S")
        rover.move()
        self.assertEqual(1, rover.y)
        self.assertEqual(1, rover.x)

        rover = Rover("1", "2", "W")
        rover.move()
        self.assertEqual(2, rover.y)
        self.assertEqual(0, rover.x)

    def test_rover_change_direction(self):
        rover = Rover("1", "2", "N")
        rover.change_direction("L")
        self.assertEqual(rover.get_direction(), "W")

        rover.change_direction("L")
        self.assertEqual(rover.get_direction(), "S")

        rover.change_direction("L")
        self.assertEqual(rover.get_direction(), "E")

        rover.change_direction("L")
        self.assertEqual(rover.get_direction(), "N")

        rover.change_direction("R")
        self.assertEqual(rover.get_direction(), "E")

        rover.change_direction("R")
        self.assertEqual(rover.get_direction(), "S")

        rover.change_direction("R")
        self.assertEqual(rover.get_direction(), "W")

        rover.change_direction("R")
        self.assertEqual(rover.get_direction(), "N")


if __name__ == '__main__':
    unittest.main()