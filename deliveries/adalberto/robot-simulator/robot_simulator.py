# Globals for the directions
# Change the values as you see fit
EAST = 2
NORTH = 1
WEST = 4
SOUTH = 3


class Robot:
    def __init__(self, direction=NORTH, x=0, y=0):
        self.direction = direction
        self.x = x
        self.y = y

    @property
    def coordinates(self):
        return (self.x, self.y)

    def move(self, comand):
        for i in comand:
            if i == "R":
                if self.direction == 4:
                    self.direction = 1
                else:
                    self.direction += 1
            if i == "L":
                if self.direction == 1:
                    self.direction = 4
                else:
                    self.direction -= 1
            if i == "A":
                if self.direction == NORTH:
                    self.y += 1
                elif self.direction == EAST:
                    self.x += 1
                elif self.direction == SOUTH:
                    self.y -= 1
                else:
                    self.x -= 1