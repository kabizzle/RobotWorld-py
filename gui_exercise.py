from coordinates import Coordinates
from robot_graphics_item import RobotGraphicsItem
from PyQt5 import QtWidgets, QtGui


class GuiExercise():
    """
    Normally these methods would be implemented in gui.py, but to make automatic
    exercise grading easier, they are implemented here.
    """

    def __init__(self, robot_world, scene, square_size):
        """
        Parameters:
        robot_world: RobotWorld of the Gui-class
        scene: The QGraphicsScene of the Gui-class
        square_size: The width and height of a single square
        """
        self.robot_world = robot_world
        self.scene = scene
        self.square_size = square_size
        self.added_robots = []


    def add_robot_world_grid_items(self):
        """
        Implement me!

        The RobotWorld already has the logical squares for the game
        and you can get these squares using its get_square method,
        but the squares for the user interface will be created here.
        This method adds an QGraphicsItem for each square in the robot world.
        Qt uses QGraphicsItems to draw objects in the QGraphicsScene.
        QGraphicsRectItem is a subclass of QGraphicsItem, and is useful for
        easily drawing rectangular items.
        This method should only be called once, otherwise it creates duplicates!

        What to do:


        1. Pseudocode:
            For each square in the RobotWorld:
                -Create a new QGraphicsRectItem with the correct position, width, and height.
                -Add the newly created item to the scene (QGraphicsScene, in other words the variable scene set in __init__).


        2. The QGraphicsItems should be positioned as follows:
            1. The top left corner (origin) of the first square should be located at (0, 0).
            2. The second square on the x-axis (1, 0) should be located at (square_size, 0).
            3. The second square on the y-axis (0, 1) should be located at (0, square_size).
            4. etc..



        3. For full points, the walls in the RobotWorld must be drawn as Dark gray
            and other squares must be drawn as Light gray. (See: RobotWorld.add_wall)

            The rgb color values must be:
            Light gray: (211, 211, 211)
            Dark gray: (20, 20, 20)



        See RobotWorld for getting the size of the world.

        Also see: https://doc.qt.io/qtforpython-5/PySide2/QtWidgets/QGraphicsItem.html
        and  https://doc.qt.io/qtforpython-5/PySide2/QtWidgets/QGraphicsRectItem.html
        and addItem() at  https://doc.qt.io/qtforpython-5/PySide2/QtWidgets/QGraphicsScene.html

        For changing the colors see:
        setBrush() at https://doc.qt.io/qtforpython-5/PySide2/QtWidgets/QAbstractGraphicsShapeItem.html
        and QBrush at https://doc.qt.io/qtforpython-5/PySide2/QtGui/QBrush.html
        and QColor at https://doc.qt.io/qtforpython-5/PySide2/QtGui/QColor.html
        """
        # Iterate over all squares in robot world
        # for x...:
            # for y...:
        x = 0
        for i in range(self.robot_world.get_width()):
            y = 0
            for j in range(self.robot_world.get_height()):
                # item = QtWidgets.QGraphicsRectItem(i, j, self.square_size, self.square_size)
                # square = self.robot_world.get_square(i,j)
                # square = item

                current = Coordinates(i,j)
                square = self.robot_world.get_square(current)   
                if square.is_wall_square():
                    colour = QtGui.QColor(20, 20, 20)
                    brush = QtGui.QBrush(colour)
                else:
                    colour = QtGui.QColor(211, 211, 211)
                    brush = QtGui.QBrush(colour)
                    
                item = QtWidgets.QGraphicsRectItem(x, y, self.square_size, self.square_size)
                item.setBrush(brush)
                self.scene.addItem(item)

                # x += self.square_size
                y += self.square_size
            x += self.square_size
                


    def add_robot_graphics_items(self):
        """
        Implement me!

        Finds all robots in the RobotWorld, which do not yet have a
        RobotGraphicsItem and adds a RobotGraphicsItem for them.
        If every robot already has a RobotGraphicsItem, this method does nothing.

        NOTE: You don't have to check if any robots have been removed from the RobotWorld

        What to do:

        1. Find all robots in the RobotWorld, which do not yet have a RobotGraphicsItem.
        2. Create RobotGraphicsItem for all such robots and add these items to the QGraphicsScene.

        Hint: You can utilize the empty self.added_robots list for checking which robots have already been added

        See: RobotGraphicsItem and RobotWorld
        """
        for i in self.robot_world.get_robots():
            robot = i
            if robot not in self.added_robots:
                robot_item = RobotGraphicsItem(robot, self.square_size)
                self.scene.addItem(robot_item)
                self.added_robots.append(robot)
