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

Ok, so what voltage to put into the L293D from the pi?
https://learn.adafruit.com/adafruit-raspberry-pi-lesson-9-controlling-a-dc-motor/lm293d

This tutorial uses 5V to power the chip from the PI...
It uses pin 18 for enable, and pins 4 and 17 for direction...
I'll try this circuit if I can't make my own one work, but now I know to use 5V...
The 5V chip power wires are bundled together, purple and green. Purple is ground.

Orange wire is enable (pos 12)

On the pi I am running ~\LegoEcho\PiDrive\driverObject.py - and nothing is happening.
I have the control lines wired into what I think are pin positions:
12,13 ans 15

I wired up when I think are the three control line to what I think are the three pins I am controlling - and unsurprisingly, something that I think it wrong.

Time for a break and to come back when I have had some sleep...

# 2019_07_07 

Ok, took a break on this to work on my ESP8266 project, but paused that now.

![](/readme_img/PiZeroPinOut.png)

Wasn't having any luck driving the motor from the pi. Lets get more simple and just flash an LED.

OK, so hooked LED up to pins 1 and 9 (3.3V and gnd)
And that lights up.

Made new test python ledFlash.py
Which should flash BCM pin 12 (GPIO 18) which I think it PWM...

Ok, even simpler, blink.py blinks an LED on pin 17
https://thepihut.com/blogs/raspberry-pi-tutorials/gpio-and-python-39-blinking-led

PWM for LED blink: https://electronicshobbyists.com/raspberry-pi-pwm-tutorial-control-brightness-of-led-and-servo-motor/

blink.py can control PWM on GPIO21 (pin 40)

https://raspi.tv/2013/rpi-gpio-0-5-2a-now-has-software-pwm-how-to-use-it
RPI GPIO support software PWM on any output

# 2019_07_14 

Having had success with PWM in blink.py, moved useful code into ledFlash.py
Got the LED flashing.
Now trying to get the motor moving for one track at 100%

I'm using GPIO 21,20,16, which are the far pins on the outside. I had 21 (pin 40) working for the LED.
GPIO 21 will be my enable pin (PWM)
The track I'm trying has three wires Purple, Blue, Green.
I think Green is enable, and runs to chip 1 (enable)
I think blue runs to chip 2 (enable 1a) and purple runs to chip 7 (enable 2a)

So, I was forgetting to power the chip as well.
3.3V to Green chip lead, gnd to purple cheap lead, and the track moved

# 2019_07_15 

I want a better way of editing on the pi. Nano sucks over ssh.

https://www.hanselman.com/blog/VisualStudioCodeRemoteDevelopmentOverSSHToARaspberryPiIsButter.aspx

first step is passwordless ssh

https://www.raspberrypi.org/documentation/remote-access/ssh/passwordless.md

just ssh-copy-id pi@trackRC.local to copy my existing key to pi.

# 2019_08_14

Running trackRC pi off tiny battery pack. Couldn't find it on the network.
Installing 
`sudo apt-get install samba winbind`

Turns out the problem is my laptop not having bonjour (e.g from iTunes) installed

What version of python should I be using?
What version is currently installed and being used on the pi?

```
pi@trackRC:~/LegoEcho/HC-SR04 $ python range.py
Distance Measurement In Progress
Waiting For Sensor To Settle
Distance: 16.46 cm
pi@trackRC:~/LegoEcho/HC-SR04 $ python --version
Python 2.7.13
```

```
pi@trackRC:~/LegoEcho/HC-SR04 $ python3 --version
Python 3.5.3
pi@trackRC:~/LegoEcho/HC-SR04 $ python3 range
python3: can't open file 'range': [Errno 2] No such file or directory
pi@trackRC:~/LegoEcho/HC-SR04 $ python3 range.py
  File "range.py", line 12
    print "Distance Measurement In Progress"
                                           ^
SyntaxError: Missing parentheses in call to 'print'
```
