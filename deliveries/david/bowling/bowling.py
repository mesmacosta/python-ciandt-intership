from collections import defaultdict

class BowlingGame:
    def __init__(self):
        self.list_bowling = list()
        self.list_points = list()

    def roll(self, pins):
        self.list_bowling.append(pins)

    def validation_roll(self):
        soma = 0
        for iterator in range(0, 2):
            soma += self.list_bowling[iterator]
            if soma == 10:
                change = self.list_bowling[iterator + 1] * 2
                self.list_bowling[iterator + 1] = change
        return self.list_bowling

    def score(self):
        gamings = 0 #defaultdict(int)
        for elements in self.validation_roll():
           gamings += elements
        return(gamings)

#
# game = BowlingGame()
# game.roll([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,10, 0])
# print(game.score())