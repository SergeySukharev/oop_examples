import pytest
import index
from math import sqrt


def test_attributes():
    tria = index.Triangle('Triangle', 5, 7, 9)

    assert tria.name == 'Triangle'
    assert tria.angles == 3
    assert tria.sideA == 5
    assert tria.sideB == 7
    assert tria.sideC == 9


@pytest.mark.parametrize('sideA, sideB, sideC', [(10, 18, 9), (14, 24, 12), (12, 24, 15)])
def test_area(sideA, sideB, sideC):
    tria = index.Triangle('tria', sideA, sideB, sideC)
    s = (sideA + sideB + sideC) / 2
    value = sqrt(s * (s - sideA) * (s - sideB) * (s - sideC))

    assert tria.area == value


@pytest.mark.parametrize('sideA, sideB, sideC', [(4, 16, 9), (3, 9, 4), (10, 100, 15)])
def test_perimeter(sideA, sideB, sideC):
    tria = index.Triangle('tria', sideA, sideB, sideC)

    assert tria.perimeter == sideA+sideB+sideC


def test_add_square():
    tria_1 = index.Triangle('Triangle', 5, 10, 7)
    tria_2 = index.Triangle('Triangle', 10, 15, 9)

    assert tria_1.add_square(tria_2) == tria_1.perimeter + tria_2.perimeter


def test_add_square_negative():
    tria_1 = index.Triangle('Triangle', 5, 10, 11)
    tria_2 = 55

    assert tria_1.add_square(tria_2) == "Argument must be instance of Figure class"
