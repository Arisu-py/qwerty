import pytest
from yandex_testing_lesson import reverse

def test_empty():
    assert reverse('') == ''

def test_one():
    assert reverse('a') == 'a'

def test_palindrom():
    assert reverse('aba') == 'aba'

def test_ordinary():
    assert reverse('abc') == 'cba'

def test_wrong_not_iter():
    with pytest.raises(TypeError):
        reverse(42)

def test_wrong_iter():
    with pytest.raises(TypeError):
        reverse(['a', 'b', 'c'])