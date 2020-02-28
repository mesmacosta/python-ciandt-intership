"""Unit testing for Car."""
import pytest
from ..main import Car


def test__check_battery_false():
    my_car = Car(manufacture="vw", model="gol", color="white", seat=5)
    assert my_car._check_battery() is False


def test__check_battery_true():
    my_car = Car(manufacture="vw", model="polo", color="white", seat=5)
    assert my_car._check_battery() is True


def test__check_alternator_false():
    my_car = Car(manufacture="vw", model="gol", color="white", seat=5)
    assert my_car._check_alternator() is False


def test__check_alternator_true():
    my_car = Car(manufacture="fiat", model="mobi", color="white", seat=5)
    assert my_car._check_alternator() is True


# #####################
# ## TESTE MELHORADO ##
# #####################
@pytest.mark.parametrize(
    "manufacture, model, expected_result",
    (
        ("vw", "gol", False),
        ("vw", "polo", True),
        ("fiat", "mobi", True),
    )
)
def test__check_battery(manufacture, model, expected_result):
    my_car = Car(manufacture=manufacture, model=model, color="white", seat=5)
    assert my_car._check_battery() is expected_result


# Fazer o teste melhorado do _check_alternator com o pessoal
# Fazer o teste unitário do _check_car_computing com o pessoal