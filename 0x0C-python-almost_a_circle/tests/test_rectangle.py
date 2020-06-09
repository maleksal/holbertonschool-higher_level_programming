''' Unittests Module '''

import sys
from io import StringIO
import unittest
from models.rectangle import Rectangle


class TestRectangleClass(unittest.TestCase):
    """ test rectangle class """

    def test_case_1(self):
        """ test id from the inherted class """

        a = Rectangle(1, 1)
        self.assertEqual(a.id, 3)

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

    def test_case_7(self):
        """ test the Rectangle area method """
        a = Rectangle(2, 3)
        self.assertEqual(a.area(), 6)

    def test_case_8(self):
        """ test with valid inputs """
        capturedOutput = StringIO()
        sys.stdout = capturedOutput

        a = Rectangle(4, 2)
        a.display()
        sys.stdout = sys.__stdout__
        valid_output = '####\n####\n'
        self.assertEqual(valid_output, capturedOutput.getvalue())

    def test_case_9(self):
        """ test with valid inputs """
        capturedOutput = StringIO()
        sys.stdout = capturedOutput

        a = Rectangle(4, 2, 1, 1)
        a.display()
        sys.stdout = sys.__stdout__
        valid_output = '\n ####\n ####\n'
        self.assertEqual(valid_output, capturedOutput.getvalue())

    def test_case_10(self):
        ''' test update method '''
        capturedOutput = StringIO()
        sys.stdout = capturedOutput

        a = Rectangle(1, 1)
        a.update(89, 2, 3, 4, 5)
        print(a, end="")

        sys.stdout = sys.__stdout__
        valid_output = '[Rectangle] (89) 4/5 - 2/3'
        self.assertEqual(valid_output, capturedOutput.getvalue())

    def test_case_11(self):
        ''' test update method with kwargs '''
        capturedOutput = StringIO()
        sys.stdout = capturedOutput

        a = Rectangle(1, 1)
        a.update(id=89, width=2, height=3, x=4, y=5)
        print(a, end="")

        sys.stdout = sys.__stdout__
        valid_output = '[Rectangle] (89) 4/5 - 2/3'
        self.assertEqual(valid_output, capturedOutput.getvalue())

if __name__ == '__main__':
    unittest.main()
