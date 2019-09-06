import unittest
import sys
sys.path.append("..") # Adds higher directory to python modules path.
sys.path.append(".")

from FlaskSoc import RangerObject 

class TestRangerObject(unittest.TestCase):


    def test_createRangerObjectUsingMock(self):
        ranger = RangerObject(23,24)
        print ranger.getDistance()
        del ranger    
        self.assertEqual('foo'.upper(), 'FOO')

'''
    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)
'''

if __name__ == '__main__':
    unittest.main()