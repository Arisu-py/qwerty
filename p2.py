import pytest
from yandex_testing_lesson import count_chars


def test_empty():
    assert count_chars('aaabb') == {'a': 3, 'b': 2}


def test_wrong_not_iter():
    with pytest.raises(TypeError):
        count_chars(42)