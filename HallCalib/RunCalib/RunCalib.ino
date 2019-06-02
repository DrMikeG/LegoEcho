
 volatile byte half_revolutions;
 unsigned int rpm;
 unsigned long timeold;

// Motor control digital output pins defined as global constants (4 wheel drive with 2 Lego motors):
const int controlPin1A = 2;                  // L293D driver input 1A on pin no 2  http://www.ti.com/lit/ds/symlink/l293.pdf connected to Arduino digital output pin 2
const int controlPin2A = 5;                  // L293D driver input 2A on pin no 7 connected to Arduino digital output pin 5
const int ENablePin = 9;                     // L293D ENable(1,2) input on pin no 1 connected to Arduino digital output pin 9

// Motor control global variables: 
int motorSpeed = 0;                          // Motor speed 0..255
int motorDirection = 1;                      // Forward (1) or reverse (0)

 void setup()
 {
   Serial.begin(9600);
   Serial.setTimeout(1000);                  // 1000 ms time out
   
   // Declare digital output pins:
   pinMode(controlPin1A, OUTPUT);      // 1A
   pinMode(controlPin2A, OUTPUT);      // 2A
   pinMode(ENablePin, OUTPUT);         // EN1,2
   digitalWrite(ENablePin, LOW);       // motor off

   // Sensor reading interrupt  
   attachInterrupt(digitalPinToInterrupt(3), magnet_detect, RISING);//Initialize the intterrupt pin (Arduino digital pin 3)
   half_revolutions = 0;
   rpm = 0;
   timeold = 0;

    for (int pwmExpSpeed = 255; pwmExpSpeed > 100; pwmExpSpeed-=10)
    {
      Serial.print("Speed: ");Serial.println(pwmExpSpeed);
      const int trials = 2;
      for (int i=0; i < trials; i++){
      unsigned int rpm = runExperiment(pwmExpSpeed,15);
        Serial.print("Trial: ");Serial.print(i);
        Serial.print(" PWM: ");Serial.print(pwmExpSpeed);
        Serial.print(" RPM: ");Serial.println(rpm);
      }
    }
 }

 void loop()//Measure RPM
 {

    
 }

// Returns the RPM averaged for the duration of the experiment...
unsigned int runExperiment(int pwmValue, int rotations)
{
    
    motorSpeed = pwmValue; // 0 to 255
    // motorSpeed = map(xValue,519,1023,0,255);
    motorDirection = 0; 
    Serial.println("Setup experiment");
    Serial.println(motorSpeed);
    SetMotorControl();        
    delay(100);

    half_revolutions = 0;
    timeold = millis();

    int mod = 0;
    while(half_revolutions < rotations)
    {
        mod++;
        if (mod == 10000)
        {
          //Serial.println("Gather data...");
          Serial.print(half_revolutions);
          Serial.print(" ,");  
          mod = 0;
        }
    }
    
    rpm = (millis() - timeold);
   
    motorSpeed = 0;
    motorDirection = 0; 
    Serial.println("Shutdown experiment");
    SetMotorControl();        
    delay(100);
   // Serial.println(rpm,DEC);
    
    return rpm;
}


 void magnet_detect()//This function is called whenever a magnet/interrupt is detected by the arduino
 {
   half_revolutions++;
   Serial.println("detect");
 }

void SetMotorControl()
/*
L293 logic:    EN1,2   1A    2A
               H       H     L    Motor turns left  (Forward; motorDirection == 1)
               H       L     H    Motor turns right (Reverse; motorDirection == 0)
Motor speed:   PWM signal on EN1,2 (490 Hz; digital output value 0..255 for motorSpeed)
*/
{
  if (motorDirection == 1)               //Forward
    {
       digitalWrite(controlPin1A, HIGH);
       digitalWrite(controlPin2A, LOW);
    }
  else                                   //Reverse
    {
       digitalWrite(controlPin1A, LOW);
       digitalWrite(controlPin2A, HIGH);
    } 
  analogWrite(ENablePin, motorSpeed);    //Speed   
}
