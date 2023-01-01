# RobotWorld

## Programming task for CS-A1123 Basics in Programming Y2 (Spring 2022)

# Features I Implemented

- add_robot_world_grid_items() function in gui_exercise.py
    -  adds a QGraphicsRectItem for each square in the GUI
- add_robot_graphics_items() function in file gui_exercise.py
    -  goes through all the robots in the RobotWorld and creates a corresponding RobotGraphicsItem for each robot for drawing
- updatePosition() method in RobotGraphicsItem class
    - updates the location of Item to correspond to the physical robot’s location
- updateRotation() in RobotGraphicsItem class
    - spins the Item to point in the direction the physical robots looks at
- updateColor() in RobotGraphicsItem class
    - paints the Item a certain color based on the current state of the physical robot
- mousePressEvent() in RobotGraphicsItem class
    - fixes a broken robot, when the robot is clicked with a mouse
