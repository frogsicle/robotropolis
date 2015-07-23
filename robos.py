"""
classes for robotropolis
"""

class ProgrammableRobot():
    """
    major solderable robots
    """
    def __init__(self):
        self.x = 0
        self.y = 0
        self.x_velocity = 0
        self.y_velocity = 0


class Solderable():
    """
    elements with inputs and outputs that can be soldered
    """
    def __init__(self):
        self.inputs = [0,0]
        self.outputs = self.logic()

    def logic(self):
        # todo, make more than or
        out = [any(self.inputs)]
        return out