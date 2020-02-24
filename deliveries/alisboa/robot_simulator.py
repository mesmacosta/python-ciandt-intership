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

    # Movimenta o robo para o norte
    def __move_north(self):
        self.y += 1

    # Movimenta o robo para o sul
    def __move_south(self):
        self.y -= 1

    # Movimenta o robo para o leste
    def __move_east(self):
        self.x += 1

    # Movimenta o robo para o oeste
    def __move_west(self):
        self.x -= 1

    # Vira o robô para a direção desejada
    def __turn(self, direction):
        self.direction = direction

    # Vira o robô para a direita
    def __turn_right(self):
        if (self.direction == NORTH):
            self.__turn(EAST)
            return
        if (self.direction == EAST):
            self.__turn(SOUTH)
            return
        if (self.direction == SOUTH):
            self.__turn(WEST)
            return
        if (self.direction == WEST):
            self.__turn(NORTH)
            return

    # Vira o robo para a esquerda
    def __turn_left(self):
        if (self.direction == NORTH):
            self.__turn(WEST)
            return
        if (self.direction == EAST):
            self.__turn(NORTH)
            return
        if (self.direction == SOUTH):
            self.__turn(EAST)
            return
        if (self.direction == WEST):
            self.__turn(SOUTH)
            return

    # Avança o robo
    def __advance(self):
        if (self.direction == NORTH):
            self.__move_north()
            return
        elif (self.direction == SOUTH):
            self.__move_south()
            return
        elif (self.direction == WEST):
            self.__move_west()
            return
        elif (self.direction == EAST):
            self.__move_east()
            return

    # Movimenta o robô
    def move(self, movement):
        for char in movement:
            if (char == 'R'):
                self.__turn_right()
                continue

            elif (char == 'L'):
                self.__turn_left()
                continue

            elif (char == 'A'):
                self.__advance()
                continue

    @property
    def coordinates(self):
        return (self.x, self.y)
