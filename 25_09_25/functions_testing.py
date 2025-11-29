import unittest
from functions import add_numbers, increment, increment_by

# Unit tests for functions.py
class TestFunctions(unittest.TestCase):

    def test_add_numbers(self): # Test for add_numbers function
        self.assertEqual(add_numbers(2, 3), 5)
        self.assertEqual(add_numbers(-1, 1), 0)
        self.assertIsInstance(add_numbers(2.5, 3.5), float)

    def test_increment(self): # Test for increment function
        self.assertEqual(increment(5), 6)
        self.assertEqual(increment(-1), 0)

    def test_increment_by(self): # Test for increment_by function
        self.assertEqual(increment_by(5, 2), 7)
        self.assertEqual(increment_by(0, 10), 10)

if __name__ == '__main__':
    unittest.main()