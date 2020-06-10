import unittest
from models.square import Square


class TestRectangleClass(unittest.TestCase):
    """ test square class """

    def test_case_1(self):
        ''' test size setter '''
        a = Square(1)
        self.assertEqual(a.size, 1)

    def test_case_2(self):
        ''' test update function '''
        a = Square(2, 1, 1, 1)
        # update method order: id, size, x, y
        a.update(2, 3, 3, 3)
        self.assertEqual(a.size, 3)
        self.assertEqual(a.x, 3)
        self.assertEqual(a.y, 3)
        self.assertEqual(a.id, 2)

    def test_case_3(self):
        ''' test to_dictionary method '''
        a = Square(4, 1, 1, 1)
        self.assertDictEqual(a.to_dictionary(), {
                    'id': 1, 'size': 4, 'x': 1, 'y': 1})
