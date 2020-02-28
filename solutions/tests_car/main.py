"""Main code for Car"""


class CarException(Exception):
    """Exception for class Car"""
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


class Car:

    def __init__(self, manufacture, model, color, seat):
        self.manufacture = manufacture
        self.model = model
        self.color = color
        self.seat = seat

    def turn_on_light(self):
        try:
            assert self._check_battery() is True
            assert self._check_alternator() is True
            assert self._check_car_computing() is True
        except Exception:
            raise CarException("Unable to turn on the light.")
        return "Light is on!"

    def _check_battery(self):
        if self.model == "gol":
            return False
        return True

    def _check_alternator(self):
        if self.manufacture == "vw":
            return False
        return True

    def _check_car_computing(self):
        if self.manufacture == "fiat" and self.seat == 4:
            return False
        return True
