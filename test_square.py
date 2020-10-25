import pytest
import index


def test_attributes():
    square = index.Figure('square', 5)

    assert square.name == 'square'
    assert square.angles == 4
    assert square.sideA == 5


@pytest.mark.parametrize('values, expected', [(4, 16), (3, 9), (10, 100)])
def test_area(values, expected):
    square = index.Figure('square', values)

    assert square.area == expected


@pytest.mark.parametrize('values, angles, expected', [(4, 4, 16), (3, 5, 15), (10, 2, 20)])
def test_perimeter(values, angles, expected):
    square = index.Figure('square', values, angles)

    assert square.perimeter == expected


def test_add_square():
    square_1 = index.Figure('square', 5)
    square_2 = index.Figure('square', 10)

    assert square_1.add_square(square_2) == square_1.perimeter + square_2.perimeter


def test_add_square_negative():
    square_1 = index.Figure('square', 5)
    square_2 = 55

    assert square_1.add_square(square_2) == "Argument must be instance of Figure class"
