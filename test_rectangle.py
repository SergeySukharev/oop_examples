import pytest
import index


def test_attributes():
    rect = index.Rectangle('rectangle', 5, 7)

    assert rect.name == 'rectangle'
    assert rect.angles == 4
    assert rect.sideA == 5
    assert rect.sideB == 7


@pytest.mark.parametrize('sideA, sideB', [(4, 16), (3, 9), (10, 100)])
def test_area(sideA, sideB):
    rect = index.Rectangle('rect', sideA, sideB)

    assert rect.area == sideA*sideB


@pytest.mark.parametrize('sideA, sideB', [(4, 4), (3, 5), (10, 2)])
def test_perimeter(sideA, sideB):
    rect = index.Rectangle('rectangle', sideA, sideB)

    assert rect.perimeter == (sideA+sideB)*2


def test_add_square():
    rect_1 = index.Rectangle('rectangle', 5, 10)
    rect_2 = index.Rectangle('rectangle', 10, 15)

    assert rect_1.add_square(rect_2) == rect_1.perimeter + rect_2.perimeter


def test_add_square_negative():
    rect_1 = index.Rectangle('rectangle', 5, 10)
    square_2 = 55

    assert rect_1.add_square(square_2) == "Argument must be instance of Figure class"
