# Write your code here :-)

import board
import busio
import time
import math

from sphero_rvr import *

import adafruit_hcsr04

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D11, echo_pin=board.D10)

rvr = RVRDrive()
rvr.wake() #turn on
rvr.set_all_leds(255,0,0) #set leds to red
time.sleep(0.1)
rvr.set_all_leds(0,255,0) #set leds to blue
time.sleep(0.1)
rvr.set_all_leds(0,0,255) #set leds to green
time.sleep(0.1) #turn off
rvr.set_all_leds(0,0,0) #turn off leds or make them all black

#Set control parameters
setpoint = 100.0
k = 3
MAX_SPEED = 100

while True:
    try:
        sensor_distance = sonar.distance

        # Add your proportional control code here.
	error = setpoint - sensor_distance 

	output = error*k


        if(output > MAX_SPEED):
            output = MAX_SPEED
        elif(output < -MAX_SPEED):
            output = -MAX_SPEED
	
	rvr.setMotors(output, output) #set the power of the motors for both the left and right track
        # Read the Sphero RVR library file to find the rvr.setMotors(left,right) command.
        # Use this command in the next line to send the output of your proportional
        # control to both the left and right motors.

    except RuntimeError:
        print("Retrying!")
        pass
    time.sleep(0.2)

