import unittest
import sys
import time

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
        # Default value is none
        self.assertEqual(None,GPIOInterface.testGetSetup(23))
        # Can set value to OUT
        GPIOInterface.setup(23,GPIOInterface.OUT)
        self.assertEqual(GPIOInterface.OUT,GPIOInterface.testGetSetup(23))
        # Can change valut to IN
        GPIOInterface.setup(23,GPIOInterface.IN)
        self.assertEqual(GPIOInterface.IN,GPIOInterface.testGetSetup(23))
        GPIOInterface.cleanup()

    def test_cleanupClearsInOurDict(self):
        #Value for pin 23 in IN
        GPIOInterface.setup(23,GPIOInterface.IN)
        self.assertEqual(GPIOInterface.IN,GPIOInterface.testGetSetup(23))
        GPIOInterface.cleanup()
        # Cleanup has cleared value
        self.assertEqual(None,GPIOInterface.testGetSetup(23))
        
    def test_OutputDefaultIsFalse(self):
        GPIOInterface.cleanup()
        self.assertEqual(False,GPIOInterface.testGetOutput(23))

    def test_OutputCanBeSetToTrue(self):
        GPIOInterface.cleanup()
        GPIOInterface.output(23,True)
        self.assertEqual(True,GPIOInterface.testGetOutput(23))

    def test_InputDefaultIsFalse(self):
        GPIOInterface.cleanup()
        self.assertEqual(False,GPIOInterface.input(23))

    def test_InputCanBeSetToTrue(self):
        GPIOInterface.cleanup()
        GPIOInterface.testSetInput(23,True)
        self.assertEqual(True,GPIOInterface.input(23))


#When Trig 23 is set as Output
#When Echo 24 is set as Input
#We set Trig to True, wait for 0.00001
#We set Trig to False

#When trigger changes from True to False, we start static timer - wait for 0.005 seconds 
#We set Echo to False
#After 0.005 seconds we set Echo to true

    def test_TestTriggerTimer(self):
        ECHO = 24
        TRIG = 23
        GPIOInterface.cleanup()
        # 24 start false
        GPIOInterface.testSetInput(ECHO,False)
        self.assertEqual(False,GPIOInterface.input(ECHO),"Echo pin should be Low")
        # Check not triggered
        self.assertEqual(False,GPIOInterface.triggerTimerStarted,"Trigger timer should not be started")
        # Pulse triggers
        GPIOInterface.output(TRIG, False)
        GPIOInterface.output(TRIG, True)
        time.sleep(0.00001)
        GPIOInterface.output(TRIG, False)

        timeAfterTrigger = time.time()
        # Check triggered
        self.assertEqual(True,GPIOInterface.triggerTimerStarted,"Trigger timer should have been started")
        # Not yet in echo pulse
        self.assertEqual(False,GPIOInterface.pulseTimerStarted,"Echo pulse timer should not be started yet")

        # Wait for start of echo pulse
        while GPIOInterface.input(ECHO)==0:
            #print "Waiting for echo timer to expire"
            timeStartOfEcho = time.time()

        delayBeforeEchoStart = timeStartOfEcho - timeAfterTrigger
        self.assertTrue(delayBeforeEchoStart > 0.25,"Delay before Echo start should be at least 0.25 seconds")
        self.assertTrue(delayBeforeEchoStart < 0.3, "Delay before Echo start should be less than 0.3 seconds")

        #Timer has expired and changes echo to true
        self.assertEqual(True,GPIOInterface.input(ECHO),"Echo has started, pin 24 should be high")
        # Pulse timer has started
        self.assertEqual(True,GPIOInterface.pulseTimerStarted,"Pulse timer should have started")
        # Wait during Echo pulse
        while GPIOInterface.input(ECHO)==1:
            timeEndOfEcho = time.time()

        #    print "Waiting for pulse timer to expire"
        self.assertEqual(False,GPIOInterface.pulseTimerStarted,"Pulse timer should have expired")
        self.assertEqual(False,GPIOInterface.triggerTimerStarted,"Trigger timer should still be expire")

        lengthOfEcho =timeEndOfEcho - timeStartOfEcho
        self.assertTrue(lengthOfEcho > 0.24,"Duration of Echo pulse should be at least 0.24 seconds")

if __name__ == '__main__':
    unittest.main()