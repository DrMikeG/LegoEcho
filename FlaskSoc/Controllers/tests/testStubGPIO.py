import unittest
import sys

# Run just me with \LegoEcho\FlaskSoc> python -m unittest Controllers.tests.testStubGPIO.TestStubGPIO

from Controllers.stubgpio import StubGPIO as GPIOInterface

class TestStubGPIO(unittest.TestCase):

    def test_GPIOInterfaceHasPropertyHIGHWhichIs1(self):
        self.assertEqual(GPIOInterface.HIGH, 1)

    def test_GPIOInterfaceHasPropertyLOWWhichIs0(self):
        self.assertEqual(GPIOInterface.LOW, 0)

    def test_GPIOInterfaceHasPropertyOUTwhichIsDifferentToPropertyIn(self):
        self.assertNotEqual(GPIOInterface.OUT, GPIOInterface.IN)


    def test_CanInitGPIOInterface(self):
        stub = GPIOInterface()
        del stub

    def test_CanSetupPin23AsOutput(self):
        GPIOInterface.setup(23,GPIOInterface.OUT)


if __name__ == '__main__':
    unittest.main()