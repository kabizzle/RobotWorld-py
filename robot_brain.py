from robot import Robot


class RobotBrain(Robot):
    """
    The class `RobotBrain` represents the "brains" (or artificial intelligence, AI) of
    virtual robots that inhabit two dimensional grid worlds. A robot brain is equipped
    with an algorithm for determining what a robot should do during its turn in a robot
    simulation. In other words, a robot brain is capable of controlling the actions of a robot body.

    Concrete class that extend this class need to provide implementations for the abstract
    `move_body` method; each such concrete class can represent a new kind of robot behavior.

    The given parameter body is the robot that the brain controls.
    """

    def __init__(self, body):
        self.body = body


    def move_body(self):
        pass
