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
            
            self.Enable_BCM = 12
            self.Ctrl1A_BCM = 13
            self.Ctrl1B_BCM = 15
            self.STUBBED = isStubbed

            if self.STUBBED == False:
                GPIO.setmode(GPIO.BCM)
                #Setup digital outs:
                GPIO.setup(self.Ctrl1A_BCM,GPIO.OUT)
                GPIO.setup(self.Ctrl1B_BCM,GPIO.OUT)
                #Setup PWM out:
                GPIO.setup(self.Enable_BCM, GPIO.OUT) # PWM pin set as output
                #self.pwm = GPIO.PWM(self.Enable_BCM, 490) # Initialize PWM on pwmPin 490Hz frequency
                self.pwm = GPIO.PWM(self.Enable_BCM, 1170) # Initialize PWM on pwmPin 1170Hz frequency
                #PWM frequency of 1.17kHz
                #Speed step 1 - duty cycle 25.8%
                #Speed step 2 - duty cycle 38.2%
                #Speed step 3 - duty cycle 50.5%
                #Speed step 4 - duty cycle 63.5%
                #Speed step 5 - duty cycle 76.1%
                #Speed step 6 - duty cycle 88.2%
                #Speed step 7 - duty cycle 100%

            #Enable_BCM = 12 
            #Ctrl1A_BCM = 13
            #Ctrl1B_BCM = 15

        def __del__(self):
            if (self.STUBBED==False):
                GPIO.cleanup()

        def driveForFive(self):
            print "Driving for 5 seconds"
            if (self.STUBBED):
                print "Mind your fingers...(Stubbed)"
            else:
                print "Mind your fingers..."
                GPIO.output(self.Ctrl1A_BCM, GPIO.HIGH)
                GPIO.output(self.Ctrl1B_BCM, GPIO.LOW)
                self.pwm.start(100)      
                time.sleep(5)
                print "Stop!"
                self.pwm.ChangeDutyCycle(0)                


def main():
    ranger = DriverObject(False)
    print ranger.driveForFive()
    del ranger

if __name__ == '__main__':main()

