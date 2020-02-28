"""Integration testing for Car."""
import pytest
from ..main import Car


def test_turn_light_on_true(mocker):
    my_car = Car(manufacture="vw", model="gol", color="white", seat=5)
    patcher = mocker.patch("tests_car.main.Car")
    patcher._check_battery.return_value = True
    patcher._check_alternator.return_value = True
    patcher._check_car_computing.return_value = True
    assert my_car.turn_on_light() is True
