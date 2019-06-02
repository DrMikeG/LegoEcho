/*
Arduino Hall Effect Sensor Project
by Arvind Sanjeev
Please check out  http://diyhacking.com for the tutorial of this project.
DIY Hacking
*/

/*
Connected the signal lead to D3
5V power & GND to the Kt-003
When magnet leaves the sensor range, pin 3 comes high, this triggers ISR magnet_detect.
RPM is the time delta in minutes * revolutions (weirdly called half_revolutions)
*/

 volatile byte half_revolutions;
 unsigned int rpm;
 unsigned long timeold;

 void setup()
 {
   Serial.begin(9600);
   // Changed to pin 3
   attachInterrupt(digitalPinToInterrupt(3), magnet_detect, RISING);//Initialize the intterrupt pin (Arduino digital pin 3)
   half_revolutions = 0;
   rpm = 0;
   timeold = 0;
 }

 void loop()//Measure RPM
 {
   if (half_revolutions >= 20) { 
     rpm = 30*1000/(millis() - timeold)*half_revolutions;
     timeold = millis();
     half_revolutions = 0;
     Serial.println(rpm,DEC);
   }
 }

 void magnet_detect()//This function is called whenever a magnet/interrupt is detected by the arduino
 {
   half_revolutions++;
   Serial.println("detect");
 }
