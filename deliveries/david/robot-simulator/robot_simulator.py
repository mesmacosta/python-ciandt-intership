# Globals for the directions
# Change the values as you see fit
EAST = 'east'
NORTH = 'north'
WEST = 'west'
SOUTH = 'south'


class Robot:
    def __init__(self, direction=NORTH, x=0, y=0):
        self.direction = direction
        self.x = x
        self.y = y

    @property
    def coordinates(self):
        return self.x, self.y

    def move(self, command):
        if command == None:
            raise ValueError("Invalid movement")
        else:
            for moving in command:
                self.returns_moviments(moving)

    def returns_moviments(self, moviment):
        if moviment == 'R':
            self.move_robo_right()
        elif moviment == 'L':
            self.move_robo_left()
        elif moviment == 'A':
            self.move_robo_advance()

    def move_robo_right(self):

        if self.direction == NORTH:
            self.direction = EAST

        elif self.direction == EAST:
            self.direction = SOUTH

        elif self.direction == SOUTH:
            self.direction = WEST

        elif self.direction == WEST:
            self.direction = NORTH

    def move_robo_left(self):

        if self.direction == NORTH:
            self.direction = WEST

        elif self.direction == WEST:
            self.direction = SOUTH

        elif self.direction == SOUTH:
            self.direction = EAST

        elif self.direction == EAST:
            self.direction = NORTH

    def move_robo_advance(self):

        if self.direction == NORTH:
            self.y += 1
        elif self.direction == SOUTH:
            self.y -= 1
        elif self.direction == EAST:
            self.x += 1
        elif self.direction == WEST:
            self.x -= 1