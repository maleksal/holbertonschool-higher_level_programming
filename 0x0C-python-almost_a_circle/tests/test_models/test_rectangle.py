''' Unittests Module '''

import unittest
from models.rectangle import Rectangle


class TestRectangleClass(unittest.TestCase):
    """ test rectangle class """

    def test_case_1(self):
        """ test id from the inherted class """

        a = Rectangle(1, 1)
        self.assertEqual(a.id, 1)
    
    def test_case_2(self):
        """ test setter for width """
        with self.assertRaises(TypeError):
            a = Rectangle("hello", 1)

        with self.assertRaises(ValueError):
            b = Rectangle(-1, 1)
    
    def test_case_3(self):
        """ test setter for height """
        with self.assertRaises(TypeError):
            a = Rectangle(1, "hello")

        with self.assertRaises(ValueError):
            b = Rectangle(1, -1)

    def test_case_4(self):
        """ test setter for x """
        with self.assertRaises(TypeError):
            a = Rectangle(1, 1, "hello")

        with self.assertRaises(ValueError):
            b = Rectangle(1, 1, -1)

    def test_case_5(self):
        """ test setter for y """
        with self.assertRaises(TypeError):
            a = Rectangle(1, 1, 1, "hello")

        with self.assertRaises(ValueError):
            b = Rectangle(1, 1, 1, -1)
    
    def test_case_6(self):
        """ test when passing no args """
        with self.assertRaises(TypeError):
            a = Rectangle()
