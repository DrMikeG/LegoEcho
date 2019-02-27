// ---------------------------------------------------------------------------
// Example NewPing library sketch that does a ping about 20 times per second.
// ---------------------------------------------------------------------------

#include <NewPing.h>
#include <Wire.h>
#include "Adafruit_LEDBackpack.h"
#include "Adafruit_GFX.h"

#define TRIGGER_PIN  11  // Arduino pin tied to trigger pin on the ultrasonic sensor.
#define ECHO_PIN     6  // Arduino pin tied to echo pin on the ultrasonic sensor.
#define MAX_DISTANCE 400 // Maximum distance we want to ping for (in centimeters). Maximum sensor distance is rated at 400-500cm.
#define BRIGHTNESS 2 // 0-15
NewPing sonar(TRIGGER_PIN, ECHO_PIN, MAX_DISTANCE); // NewPing setup of pins and maximum distance.

Adafruit_AlphaNum4 alpha4 = Adafruit_AlphaNum4();

void setup() {
  Serial.begin(115200); // Open serial monitor at 115200 baud to see ping results.
  alpha4.begin(0x70);  // pass in the address
  alpha4.setBrightness(BRIGHTNESS);
}

char displaybuffer[4] = {' ', ' ', ' ', ' '};
bool dpUsed[4] = {false,false,false,false};

void loop() {
  delay(500);                      // Wait 50ms between pings (about 20 pings/sec). 29ms should be the shortest delay between pings.
  unsigned int uS = sonar.ping(); // Send ping, get ping time in microseconds (uS).
  Serial.print("Ping: ");

  float distanceInCM = uS / US_ROUNDTRIP_CM;
  //Serial.print(distanceInCM); // Convert ping time to distance in cm and print result (0 = outside set distance range)
  //Serial.println("cm");

  bool shouldRedraw = false;

  dpUsed[0] = false;
  dpUsed[1] = false;
  dpUsed[2] = false;
  dpUsed[3] = false;
  displaybuffer[0] = ' ';
  displaybuffer[1] = ' ';
  displaybuffer[2] = ' ';
  displaybuffer[3] = ' ';

  if (distanceInCM <= 0.0)
  {    
    // Display nothing...      
  }
  else if (distanceInCM < 10.0)
  {
    // up to 9.9cm..
     unsigned int cmRounded = (10*distanceInCM); // Get first decimal place as int.
     // eg. 9.8 become 98...     
     char buf[12]; // "-2147483648\0"
     itoa(cmRounded, buf, 10);
     displaybuffer[0] = buf[0]; // e.g 9
     dpUsed[0] = true;         // include . 
     displaybuffer[1] = buf[1]; // e.g 8
     displaybuffer[2] = 'c';
     displaybuffer[3] = 'm';
     shouldRedraw = true;
  }
  else if (distanceInCM < 100)
  {
    // up to 99cm
      unsigned int cmRounded = distanceInCM;
      char buf[12]; // "-2147483648\0"
      itoa(cmRounded, buf, 10);
      displaybuffer[0] = buf[0];
      displaybuffer[1] = buf[1];
      displaybuffer[2] = 'c';
      displaybuffer[3] = 'm';
      shouldRedraw = true;
  }
  else if (distanceInCM < 1000)
  {
    //eg 123cm
    unsigned int cmRounded = distanceInCM;
      char buf[12]; // "-2147483648\0"
      itoa(cmRounded, buf, 10);
      displaybuffer[0] = buf[0]; // e.g 1
      dpUsed[0] = true;         // include . 
      displaybuffer[1] = buf[1]; // e.g. 2
      displaybuffer[2] = buf[2]; // e.g 3
      displaybuffer[3] = 'm';
      shouldRedraw = true;
  }

  if (shouldRedraw)
  {
    // set every digit to the buffer
    alpha4.writeDigitAscii(0, displaybuffer[0],dpUsed[0]);
    alpha4.writeDigitAscii(1, displaybuffer[1],dpUsed[1]);
    alpha4.writeDigitAscii(2, displaybuffer[2],dpUsed[2]);
    alpha4.writeDigitAscii(3, displaybuffer[3],dpUsed[3]);
     // write it out!
    alpha4.writeDisplay();
  }
}


