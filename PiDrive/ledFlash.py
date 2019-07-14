import time
import RPi.GPIO as GPIO

#const int controlPin1A = 2;                  // L293D driver input 1A on pin no 2  http://www.ti.com/lit/ds/symlink/l293.pdf connected to Arduino digital output pin 2
#const int controlPin2A = 5;                  // L293D driver input 2A on pin no 7 connected to Arduino digital output pin 5
#const int ENablePin = 9;                     // L293D ENable(1,2) input on pin no 1 connected to Arduino digital output pin 9


#void SetMotorControl()

#L293 logic:    EN1,2   1A    2A
#               H       H     L    Motor turns left  (Forward; motorDirection == 1)
#               H       L     H    Motor turns right (Reverse; motorDirection == 0)
#Motor speed:   PWM signal on EN1,2 (490 Hz; digital output value 0..255 for motorSpeed)
#{
#  if (motorDirection == 1)               //Forward
#    {
#       digitalWrite(controlPin1A, HIGH);
#       digitalWrite(controlPin2A, LOW);
#    }
#  else                                   //Reverse
#    {
#       digitalWrite(controlPin1A, LOW);
#       digitalWrite(controlPin2A, HIGH);
#    } 
#  analogWrite(ENablePin, motorSpeed);    //Speed   
#}


class DriverObject:
        def __init__(self,isStubbed=False):
            
            self.Enable_BCM = 21
            self.controlPin1A = 20
            self.controlPin2A = 16
            GPIO.setmode(GPIO.BCM)
            #Setup PWM out:
            GPIO.setup(self.Enable_BCM, GPIO.OUT) # PWM pin set as output
            GPIO.setup(self.controlPin1A, GPIO.OUT)   # Declaring pin 20 as output pin
            GPIO.setup(self.controlPin2A, GPIO.OUT)   # Declaring pin 16 as output pin
            self.pwm = GPIO.PWM(self.Enable_BCM, 490) # Initialize PWM on pwmPin 490Hz frequency

        def __del__(self):
                GPIO.cleanup()

        def driveForFive(self):
            self.pwm.start(0)
            try:
		# fade in from min to max in increments of 5 points:
        	print "FLASHING for 5 seconds"
                GPIO.output(self.controlPin1A,GPIO.HIGH)
                GPIO.output(self.controlPin2A,GPIO.LOW)
                print "attempting to set duty cycle"
                self.pwm.ChangeDutyCycle(99)
		while 1:
			time.sleep(50)

            except KeyboardInterrupt:
                pass        # Go to next line
            self.pwm.stop()      # Stop the PWM
            GPIO.cleanup()  # Make all the output pins LOW

def main():
    ranger = DriverObject(False)
    print ranger.driveForFive()
    del ranger

if __name__ == '__main__':main()

