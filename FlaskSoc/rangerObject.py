import RPi.GPIO as GPIO
import time
import random

class RangerObject:
        def __init__(self,trigPinBCM=None,echoPinBMC=None,isStubbed=False):
            self.TRIG = 23
            if trigPinBCM != None:
                self.TRIG = trigPinBCM
            self.ECHO = 24
            if echoPinBMC !=  None:
                self.ECHO = echoPinBMC
            self.STUBBED = isStubbed

            if self.STUBBED == False:
                GPIO.setmode(GPIO.BCM)
                GPIO.setup(self.TRIG,GPIO.OUT)
                GPIO.setup(self.ECHO,GPIO.IN)
#TRIG = 23 
#ECHO = 24

        def __del__(self):
            if (self.STUBBED==False):
                GPIO.cleanup()

        def getDistance(self):
            print "Distance Measurement In Progress"
            if (self.STUBBED):
                value = random.randint(1,101)
            else:
                GPIO.output(self.TRIG, False)
                print "Waiting For Sensor To Settle"
                time.sleep(2)
                GPIO.output(self.TRIG, True)
                time.sleep(0.00001)
                GPIO.output(self.TRIG, False)

                while GPIO.input(self.ECHO)==0:
                	pulse_start = time.time()

                while GPIO.input(self.ECHO)==1:
                	pulse_end = time.time()
                pulse_duration = pulse_end - pulse_start
                distance = pulse_duration * 17150
               	value = round(distance, 2)
                print "Distance:",value,"cm"
	    return value


def main():
    ranger = RangerObject(23,24,False)
    print ranger.getDistance()
    del ranger

if __name__ == '__main__':main()

