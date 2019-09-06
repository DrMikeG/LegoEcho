import time
import random

import sys
sys.path.append(".")

try:
    import RPi.GPIO as GPIOInterface
except ImportError:
    print "Using Stub GPIOInterface"
    from FlaskSoc import StubGPIO as GPIOInterface


class RangerObject:
        def __init__(self,trigPinBCM=None,echoPinBMC=None):
            self.TRIG = 23
            if trigPinBCM != None:
                self.TRIG = trigPinBCM
            self.ECHO = 24
            if echoPinBMC !=  None:
                self.ECHO = echoPinBMC
            
            GPIOInterface.setmode(GPIOInterface.BCM)
            GPIOInterface.setup(self.TRIG,GPIOInterface.OUT)
            GPIOInterface.setup(self.ECHO,GPIOInterface.IN)
#TRIG = 23 
#ECHO = 24

        def __del__(self):
                GPIOInterface.cleanup()

        def getDistance(self):
            print "Distance Measurement In Progress"
            GPIOInterface.output(self.TRIG, False)
            print "Waiting For Sensor To Settle"
            time.sleep(2)
            GPIOInterface.output(self.TRIG, True)
            time.sleep(0.00001)
            GPIOInterface.output(self.TRIG, False)

            while GPIOInterface.input(self.ECHO)==0:
                pulse_start = time.time()

            while GPIOInterface.input(self.ECHO)==1:
                pulse_end = time.time()
            pulse_duration = pulse_end - pulse_start
            distance = pulse_duration * 17150
            value = round(distance, 2)
            print "Distance:",value,"cm"
	    return value


def main():
    ranger = RangerObject(23,24)
    print ranger.getDistance()
    del ranger

if __name__ == '__main__':main()

