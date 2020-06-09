''' Unittest Module '''

import unittest
from models.base import Base

class TestBaseClass(unittest.TestCase):
    ''' test base class '''

    def test_1(self):
        ''' if id not none, instance id should be 12 '''
        a = Base(12)
        self.assertEqual(a.id, 12)
    
    def test_2(self):
        ''' when id is None, instance id should be 1 '''
        a = Base()
        self.assertEqual(a.id, 1)
    
    def test_2(self):
        ''' id should increment to 2 '''
        a = Base()
        b = Base()
        self.assertEqual(b.id, 2)




if __name__ == '__main__':
    unittest.main()
