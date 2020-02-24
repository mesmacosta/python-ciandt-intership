# Globals for the directions
# Change the values as you see fit
EAST = 1
NORTH = 0
WEST = 3
SOUTH = 2


class Robot:
    def __init__(self, direction=NORTH, x=0, y=0):
        self.direction = direction
        self.x = x
        self.y = y
        pass
    def move(self, movimento):
        for i in movimento:
            if i == "R":
                if self.direction != 3:
                   self.direction = self.direction + 1
                else:
                    self.direction = 0
            if i == "L":
                if self.direction != 0:
                   self.direction = self.direction - 1
                else:
                    self.direction = 3
            if i == "A":
                if self.direction == NORTH:
                    self.y = self.y + 1
                elif self.direction == SOUTH:
                    self.y = self.y - 1
                elif self.direction == WEST:
                    self.x = self.x - 1
                elif self.direction == EAST:
                    self.x = self.x + 1
    @property
    def coordinates(self):
        return (self.x, self.y)