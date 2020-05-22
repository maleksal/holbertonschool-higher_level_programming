"""
unit test for max_integer function"""
import unittest

max_integer = __import__('6-max_integer').max_integer

class TestMaximumInteger(unittest.TestCase):
    '''unit testing class'''

    def test_with_no_input(self):
        self.assertEqual(max_integer(), None)

    def test_valid_input(self):
        lst = [1, 2, 3, 50]
        self.assertEqual(max_integer(lst), 50)

    def test_mixed_integers(self):
        lst = [-1, -2, 3, -50]
        self.assertEqual(max_integer(lst), 3)

    def test_non_valid_list(self):
        lst = ['hello', 0, 0, 0]
        with self.assertRaises(TypeError):
            max_integer(lst)

if __name__ == "__main__":
    unittest.main()