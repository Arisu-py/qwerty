import pytest
from yandex_testing_lesson import Rectangle


def test_one_step():
    assert Rectangle(2, 3)


def test_area():
    assert Rectangle(2, 3).get_area() == 6


def test_p():
    assert Rectangle(2, 3).get_perimeter() == 10


def test_wrong():
    with pytest.raises(TypeError):
        Rectangle('a', 1)


def test_wrong_n():
    with pytest.raises(ValueError):
        Rectangle(-1, 2)


def test_wrong_1():
    with pytest.raises(TypeError):
        Rectangle(1, 'a')


def test_wrong_n1():
    with pytest.raises(ValueError):
        Rectangle(2, -1)

