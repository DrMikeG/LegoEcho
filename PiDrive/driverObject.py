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
            self.Ctrl1A_BCM = 16
            self.Ctrl1B_BCM = 20
            self.STUBBED = isStubbed

            if self.STUBBED == False:
                GPIO.setmode(GPIO.BCM)
                #Setup digital outs:
                GPIO.setup(self.Ctrl1A_BCM,GPIO.OUT)
                GPIO.setup(self.Ctrl1B_BCM,GPIO.OUT)
                #Setup PWM out:
                self.pwm = GPIO.PWM(Enable_BCM, 490) # Initialize PWM on pwmPin 490Hz frequency

            #Enable_BCM = 12 
            #Ctrl1A_BCM = 16
            #Ctrl1B_BCM = 20

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
                pwm.ChangeDutyCycle(0)                


def main():
    ranger = DriverObject(False)
    print ranger.driveForFive()
    del ranger

if __name__ == '__main__':main()

