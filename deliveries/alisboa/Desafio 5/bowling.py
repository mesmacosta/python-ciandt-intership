class BowlingGame:
    def __init__(self):
        self.point_rolls = []
        self.intermediate_roll = None
        self.actual_roll = 0

    def roll(self, pins):
        if pins < 0:
            raise Exception("Cannot score negative points")
        if pins > 10:
            raise Exception("Cannot score more than 10 points")
        if self.intermediate_roll:
            if self.intermediate_roll + pins > 10:
                raise Exception("Cannot score more than 10 points in a frame")
        if self.actual_roll >= 20 and not (self.point_rolls[9]['strike'] or self.point_rolls[9]['spare']):
            raise Exception("test_cannot_roll_if_game_already_has_ten_frames")
        if self.actual_roll >= 21 and not (self.point_rolls[9]['strike']):
            raise Exception("test_cannot_roll_after_bonus_roll_for_spare")
        if self.actual_roll >= 22:
            raise Exception("test_cannot_roll_after_bonus_rolls_for_strike")

        if pins == 10:
            roll = {
                'points': 10,
                'roll_1': 10,
                'roll_2': 0,
                'strike': True,
                'spare': False
            }
            self.point_rolls.append(roll)
            self.intermediate_roll = None
            if self.actual_roll >= 20:
                self.actual_roll += 1
            else:
                self.actual_roll += 2
            return

        if self.intermediate_roll is not None:
            is_spare = self.intermediate_roll + pins == 10
            roll = {
                'points': pins + self.intermediate_roll,
                'roll_1': self.intermediate_roll,
                'roll_2': pins,
                'strike': False,
                'spare': is_spare
            }
            self.point_rolls.append(roll)
            self.intermediate_roll = None
            self.actual_roll += 1
            return

        self.intermediate_roll = pins
        self.actual_roll += 1

    def score(self):
        for index_element in range(10):
            if self.point_rolls[index_element]['spare']:
                try:
                    self.point_rolls[index_element]['points'] += self.point_rolls[index_element + 1]['roll_1']
                except IndexError:
                    self.point_rolls[index_element]['points'] += self.intermediate_roll
            if self.point_rolls[index_element]['strike']:
                if not self.point_rolls[index_element + 1]['strike']:
                    self.point_rolls[index_element]['points'] += self.point_rolls[index_element + 1]['roll_1'] + \
                                                             self.point_rolls[index_element + 1]['roll_2']
                else:
                    try:
                        self.point_rolls[index_element]['points'] += self.point_rolls[index_element + 1]['roll_1'] + \
                                                                 self.point_rolls[index_element + 2]['roll_1']
                    except IndexError:
                        self.point_rolls[index_element]['points'] += self.point_rolls[index_element + 1]['roll_1'] + \
                                                                     self.intermediate_roll

        return sum([self.point_rolls[index_element]['points'] for index_element in range(10)])
