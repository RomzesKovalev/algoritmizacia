import unittest


class stackoperations(unittest.TestCase):
    def test_nonempty(self):
        stack = []
        self.assertTrue(len(stack) == 0, 'стэк не пуст')

    def test_empty(self):
        stack = ['bibip']
        self.assertFalse(len(stack) == 0, 'стэк пуст')


if __name__ == "__main__":
    unittest.main()

