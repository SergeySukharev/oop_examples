import pytest
import index
from math import pi


def test_attributes():
    circle = index.Circle('circle', 8)

    assert circle.name == 'circle'
    assert circle.sideA == 8


@pytest.mark.parametrize('sideA', [7, 100, 22])
def test_area(sideA):
    circle = index.Circle('circle', sideA)
    value = pi * sideA ** sideA

    assert circle.area == value


@pytest.mark.parametrize('sideA', [10, 123, 9])
def test_perimeter(sideA):
    circle = index.Circle('circle', sideA)
    value = 2 * pi * sideA

    assert circle.perimeter == value


def test_add_square():
    circle_1 = index.Circle('circle', 8)
    circle_2 = index.Circle('circle', 12)

    assert circle_1.add_square(circle_2) == circle_1.perimeter + circle_2.perimeter


def test_add_square_negative():
    circle_1 = index.Circle('circle', 8)
    square_2 = 55

    assert circle_1.add_square(square_2) == "Argument must be instance of Figure class"
