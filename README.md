# LegoEcho
Hack to add echo location obstacle avoidance to Lego RC tracked racer

First off, saving some old code, before I start anything new.

Secondly, recording some URLs:

https://www.hackster.io/Notthemarsian/take-control-over-lego-power-functions-ee0bfa
(this is the place for me to start)

https://www.theengineeringprojects.com/2017/07/introduction-to-l293d.html

# 2019_07_02 
Ok, coming back to this after a while.
The last thing I was working on was HallCalib - using a hall effects sensor to measure speed.
I think I burnt out one of the motors, so I have replaced it.

Now I want to get back to driving it from the pi, using the FlaskSoc website.

I have a pi (see FlaskSock), which I can boot and get into...

Setting this up on trackRC
ssh pi@trackrc.local / trackRC

I have a prototoboard with a driver chip on, with 8 wires, I can't quite remember the purpose of..

Thankfully I have...
![alt tag](/readme_img/chip.jpg) 

To remind me that:
The 9V input comes from a lego lead that connects to the battery pack
5Volts/GND needs to come from the PI /arduino

Should I be driving this chip at 3V not 5V?

6 control wires, 3 for each track.

So, looking at
![alt tag](/readme_img/pinout.png) 

I've already got a range finder using:
2,6,16,18

I need pins 4 and 9 to power the chip

There are two enable pins which require PWM for analog writes:
There are 4 direction pins which can just be digital writes:
```
const int controlPin1A = 2;                  // L293D driver input 1A on pin no 2  http://www.ti.com/lit/ds/symlink/l293.pdf connected to Arduino digital output pin 2
const int controlPin2A = 5;                  // L293D driver input 2A on pin no 7 connected to Arduino digital output pin 5
const int ENablePin = 9;                     // L293D ENable(1,2) input on pin no 1 connected to Arduino digital output pin 9
// Servo control digital output pins defined as global constants (Servo steering with 1 Lego servo):
const int controlPin3A = 6;                  // L293D driver input 3A on pin no 10 connected to Arduino digital output pin 6
const int controlPin4A = 8;                  // L293D driver input 4A on pin no 15 connected to Arduino digital output pin 8 
const int servoENablePin = 3;        
```

Looking at the pinouts, I think 

32 (GPIO 12, wiring 26, BMC 12), is PWM0
35 (GPIO 19, wiring 24, BCM 19), is PWM1

I want to wire up and run one tread...

