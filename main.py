import sys
from PyQt5.QtWidgets import QApplication

from gui import GUI

from direction import Direction
from robotworld import *
from coordinates import *
from robot import *
from spinbot import *
from drunkbot import *
from nosebot import *
from lovebot import *


def main():
    """
    Creates a RobotWorld, adds robots and launches the Graphical User Interface.

    Use this for testing your code.

    You can modify this however you like.
    """
    test_world = RobotWorld(10, 8)
    wall1_coordinates = Coordinates(2, 4)
    test_world.add_wall(wall1_coordinates)
    wall2_coordinates = Coordinates(0, 5)
    test_world.add_wall(wall2_coordinates)

    nose_location = Coordinates(9, 7)
    nose_body = Robot('Nose')
    nose_brain = Nosebot(nose_body)
    nose_body.set_brain(nose_brain)
    test_world.add_robot(nose_body, nose_location, Direction.EAST)

    spin_location = Coordinates(2, 3)
    spin_body = Robot('Spin')
    spin_brain = Spinbot(spin_body)
    spin_body.set_brain(spin_brain)
    test_world.add_robot(spin_body, spin_location, Direction.SOUTH)

    love_location = Coordinates(8, 5)
    love_body = Robot('Love')
    love_brain = Lovebot(love_body, spin_body)
    love_body.set_brain(love_brain)
    test_world.add_robot(love_body, love_location, Direction.EAST)

    drunk_location = Coordinates(5, 5)
    drunk_body = Robot('Drunk')
    seed = 2
    drunk_brain = Drunkbot(drunk_body, seed)
    drunk_body.set_brain(drunk_brain)
    test_world.add_robot(drunk_body, drunk_location, Direction.EAST)

    # Every Qt application must have one instance of QApplication.
    global app # Use global to prevent crashing on exit
    app = QApplication(sys.argv)
    gui = GUI(test_world, 50)

    # Start the Qt event loop. (i.e. make it possible to interact with the gui)
    sys.exit(app.exec_())

    # Any code below this point will only be executed after the gui is closed.


if __name__ == "__main__":
    main()
