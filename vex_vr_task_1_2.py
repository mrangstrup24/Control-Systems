# Library imports
from vexcode import *
from math import *
from random import randint


drivetrain = Drivetrain()
magnet = Electromagnet("magnet", 0)
pen = Pen()
brain = Brain()
left_bumper = Bumper("leftBumper", 1)
right_bumper = Bumper("rightBumper", 2)
distance = Distance()
front_eye = EyeSensor("fronteye", 3)
down_eye = EyeSensor("downeye", 4)
location = Location()


def driveXDistance(setpoint,duration):
    # reset the timer
    brain.timer_reset()
    maxSpeed = 100
    k = 1

    # loop while the timer is less than the duration input of the function.
    while(brain.timer_time(SECONDS)<duration):
        # Your code goes here!
        currentXLocation = location.position(X,MM)
        error = setpoint - currentXLocation
        output = k*error
        # Ensure the output is not more than the maximum speed
        if(output>maxSpeed):
            output = maxSpeed
        elif(output<-maxSpeed):
            output = -maxSpeed
        drivetrain.drive(FORWARD)
        drivetrain.set_drive_velocity(output,PERCENT)



        #VEXCode VR requires that we have a small pause in any loop we run.    
        wait(1,MSEC)
    drivetrain.stop()

def driveYDistance(setpoint,duration):
    # reset the timer
    brain.timer_reset()

    maxSpeed = 100
    k = 1

    # loop while the timer is less than the duration input of the function.
    while(brain.timer_time(SECONDS)<duration):
        # Your code goes here!
        currentYLocation = location.position(Y,MM)
        error = setpoint - currentYLocation
        output = k*error
        # Ensure the output is not more than the maximum speed
        if(output>maxSpeed):
            output = maxSpeed
        elif(output<-maxSpeed):
            output = -maxSpeed
        drivetrain.drive(FORWARD)
        drivetrain.set_drive_velocity(output,PERCENT)








        #VEXCode VR requires that we have a small pause in any loop we run.    
        wait(1,MSEC)
    drivetrain.stop()


def driveDiagDistance(setpoint,duration):
    # reset the timer
    brain.timer_reset()

    maxSpeed = 100
    k = 1

    # loop while the timer is less than the duration input of the function.
    while(brain.timer_time(SECONDS)<duration):
        # Your code goes here!
        currentXLocation = location.position(X,MM)
        error = setpoint - currentXLocation
        output = k*error
        # Ensure the output is not more than the maximum speed
        if(output>maxSpeed):
            output = maxSpeed
        elif(output<-maxSpeed):
            output = -maxSpeed
        drivetrain.drive(FORWARD)
        drivetrain.set_drive_velocity(output,PERCENT)









        #VEXCode VR requires that we have a small pause in any loop we run.    
        wait(1,MSEC)
    drivetrain.stop()

# Add project code in "main"
def main():
    pen.move(DOWN)
    drivetrain.turn_to_heading(90,DEGREES,wait=True)
    driveXDistance(0,3)
    drivetrain.turn_to_heading(0,DEGREES,wait=True)
    driveYDistance(0,3)
    drivetrain.turn_to_heading(45,DEGREES,wait=True)
    driveDiagDistance(400,4)
# VR threads — Do not delete
vr_thread(main())
