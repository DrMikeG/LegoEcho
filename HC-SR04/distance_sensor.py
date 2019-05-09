#!/usr/bin/python
#https://pimylifeup.com/raspberry-pi-distance-sensor/
import RPi.GPIO as GPIO
import time

try:
      #GPIO.setmode(GPIO.BOARD)
      #PIN_TRIGGER = 7
      #PIN_ECHO = 11

      GPIO.setmode(GPIO.BCM)
      PIN_TRIGGER = 23 
      PIN_ECHO = 24

      GPIO.setup(PIN_TRIGGER, GPIO.OUT)
      GPIO.setup(PIN_ECHO, GPIO.IN)

      GPIO.output(PIN_TRIGGER, GPIO.LOW)

      print "Waiting for sensor to settle"

      time.sleep(2)

      print "Calculating distance"


      # The HC-SR04 sensor requires a short 10uS pulse to trigger the module, 
      # which will cause the sensor to start the ranging program 
      # (8 ultrasound bursts at 40 kHz) in order to obtain an echo response. 
      # So, to create our trigger pulse, we set out trigger pin high for 10uS then set it low again.
      GPIO.output(PIN_TRIGGER, GPIO.HIGH)

      time.sleep(0.00001)

      GPIO.output(PIN_TRIGGER, GPIO.LOW)

      while GPIO.input(PIN_ECHO)==0:
            pulse_start_time = time.time()
      while GPIO.input(PIN_ECHO)==1:
            pulse_end_time = time.time()

      pulse_duration = pulse_end_time - pulse_start_time
      distance = round(pulse_duration * 17150, 2)
      print "Distance:",distance,"cm"

finally:
      GPIO.cleanup()