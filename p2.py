import unittest
from yandex_testing_lesson import reverse


class TestReverse(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(reverse(''), '')
    def test_one(self):
        self.assertEqual(reverse('a'), 'a')
    def test_palindrom(self):
        self.assertEqual(reverse('aba'), 'aba')
    def test_ordinary(self):
        self.assertEqual(reverse('abcde'), 'edcba')
    def test_wrong_not_iter(self):
        with self.assertRaises(TypeError):
            reverse(42)
    def test_wrong_iter(self):
        with self.assertRaises(TypeError):
            reverse(['a', 'b', 'c'])


if __name__ == '__main__':
     unittest.main()