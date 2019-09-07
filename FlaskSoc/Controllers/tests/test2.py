import unittest
import sys

from Controllers.rangerobject import RangerObject
from Controllers.stubgpio import StubGPIO as GPIOInterface

class TestRangerObject(unittest.TestCase):

    def test_createRangerObjectUsingMock(self):
        ranger = RangerObject(23,24)
        del ranger    

    def test_RangerObjectGetDistance(self):
        ranger = RangerObject(23,24)
        print ranger.getDistance()
        del ranger    
        self.assertEqual('foo'.upper(), 'FOO')

if __name__ == '__main__':
    unittest.main()