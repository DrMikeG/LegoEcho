
 volatile byte detections;
 unsigned int rpm;
 unsigned long timeold;
 unsigned long timenew;

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
   detections = 0;
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
    motorDirection = 1; 
    //Serial.println("Setup experiment");
    //Serial.println(motorSpeed);
    SetMotorControl();        
    delay(100);

    long* trialTimes = new long[rotations]; 

    // No detections
    //Serial.println("Waiting for magnet 0 pass...");
    detections = 0;
    while (detections < 1) {
      // wait for first detect to start experiment...
    }
    
    // detection is now equal to 1
    //Serial.print("Detections: ");
    //Serial.println(detections);
    
    timeold = millis();

    for (int t=0; t < rotations; t++)
    {
        //Serial.print("Waiting for magnet pass ");
        //Serial.println(t);
        while(detections < (t+2))
        { 
          // wait for next detection
        }
        timenew = millis();
        // calculate time
        trialTimes[t] = timenew - timeold;
        //Serial.print("Time: ");
        //Serial.println(trialTimes[t]);
        // swap times
        timeold = timenew;
    }

    motorSpeed = 0;
    motorDirection = 1; 
    //Serial.println("Shutdown experiment");
    SetMotorControl();        
    delay(100);
    
    // We now have [rotations] times which should be similar... (although might contain double counting)

    // Sort,
    // Find the median, 
    // Find the sum
    // 

    bubbleSort(trialTimes,rotations); // Using bubble sort offends me deeply.
    
    long median =trialTimes[rotations/2]; 
    long sumValue = sum(trialTimes,rotations);

    if (true)
    {
    Serial.println("");
    Serial.print("Max Number: ");
    Serial.print(trialTimes[rotations-1]);
    Serial.println("");

    Serial.print("Medium Number: ");
    Serial.print(median);
    Serial.println("");
  
    Serial.print("Min Number: ");
    Serial.print(trialTimes[0]);
    Serial.println("");

    Serial.print("Sum: ");
    Serial.print(sumValue);
    Serial.println("");
    }
    // How many rotations do we think we have done?

    float estRotations = sumValue / (float)median;
    
    float timeForRotation = sumValue / estRotations;    
    
    rpm = (unsigned int)(60000 / timeForRotation);

    if (true)
    {
    Serial.print("Estimated rotations made: ");
    Serial.println(estRotations);
    
    Serial.print("Estimate MS for one rotation: ");
    Serial.println(timeForRotation);
    Serial.print("Estimate rpm: ");
    Serial.println(rpm);
    }
    
    delete [] trialTimes;
    
    return rpm;
}


 void magnet_detect()//This function is called whenever a magnet/interrupt is detected by the arduino
 {
   detections++;
   //Serial.println("detect");
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

long sum(long a[], int size) {
  long sumValue = 0;
  for(int i=0; i<(size-1); i++) {
    sumValue += a[i];
  }
  return sumValue;
}

void bubbleSort(long a[], int size) {
    for(int i=0; i<(size-1); i++) {
        for(int o=0; o<(size-(i+1)); o++) {
                if(a[o] > a[o+1]) {
                    int t = a[o];
                    a[o] = a[o+1];
                    a[o+1] = t;
                }
        }
    }
}
