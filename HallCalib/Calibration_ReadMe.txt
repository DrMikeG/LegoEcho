I want to calibrate my lego motors and track speed relative to the supplied PWM.

I'm going to try and do this using a hall effect sensor I have handy.
https://uk.banggood.com/Hall-Effect-Magnetic-Sensor-Module-DC-5V-For-Arduino-p-76469.html?gmcCountry=GB&currency=GBP&createTmp=1&utm_source=googleshopping&utm_medium=cpc_bgcs&utm_content=garman&utm_campaign=pla-gbg-ele-diy2-pc&ad_id=339489662626&gclid=CjwKCAjw583nBRBwEiwA7MKvoEN80sRxPXYdXpE3uz2A-thCk6mDLDyd040wFkPJOQAZjcJEEziOJBoC4JYQAvD_BwE&cur_warehouse=CN

https://maker.pro/arduino/tutorial/how-to-use-a-hall-effect-sensor-with-arduino

You can just define pin 2 as INPUT_PULLUP and then you don't need the 10k pullup resistor. Make sure you define the pin before attaching the interrupt.

ie.  

pinMode(2, INPUT_PULLUP);

attachInterrupt(0, magnet_detect, RISING);  //Initialize the intterrupt pin (Arduino digital pin 2)

This uses the internal pullup resistor in the Arduino.

KY-003
Built in resistor and LED

https://rydepier.wordpress.com/2014/12/23/using-a-hall-effect-sensor-with-arduino/


First - used ky-003 test sketch for simple magnet magnet_detect
Second used ArduinoHallEffect test sketch to test RPM calculation with digital interrupt

Third, need to drive the track again..