from SpacecraftSim import SpacecraftEngine

'''
Spacecraft Engine API:

myRocket.getData(): 
inputs: none
outputs: an array with position, velocity, and acceleration as the first, second, and third elements.

myRocket.update():
inputs: none
outputs: none
purpose: Gets a new set of position, velocity, and acceleration for each loop.

myRocket.setThrust(signal):
inputs: thrust (percent of maximum) as a signal from 0 - 100
outputs: none
purpose: Sets the thrust of the engine 

myRocket.checkCrashStatus():
inputs: none
outputs: True or False indicating whether or not the rocket has crashed. This occurs if the rocket hits the ground with a velocity greater than 1.5 m/s.

myRocket.checkLandingStatus():
inputs: none
outputs: True or False indicating whether or not the rocket has landed. This occurs if the rocket's height hits Zero

myRocket.getLandingVel():
inputs: none
outputs: speed of the rocket upon landing.




'''

myRocket = SpacecraftEngine()

currentTime = 0.0
currentThrust = 0
accumulatedError = 0.0
SIMULATION_TIME = 60.0 #seconds of simulation

# k = 0.000301
# k2 = 0.11
# k3 = 4.2

k = 0
k2 = 0
k3 = 0


while(currentTime < SIMULATION_TIME):
  rocketData = myRocket.getData() #data for rocket
  print(currentTime,",",rocketData[0])  
  myRocket.update() #Get update from rocket over radio
  currentTime += 0.1 # Don't change me

#rocketData[1]*k

#(300-rocketData[0])*k + rocketData[1]*-k2 + 

  #Your code goes here
  # myRocket.setThrust(rocketData[2]*-k3 + rocketData[1]*-k2 + (300-rocketData[0])*k)

  myRocket.setThrust(((300-rocketData[0])/1000)**2)

  


#Don't change anything below this line.
if(myRocket.checkLandingStatus()):
  if(myRocket.checkCrashStatus() == True):
    print("Rocket has crashed")
    print("Landing speed was " + str(myRocket.getLandingVel()) + " m/s")
  else:
    print("Hooray - the rocket landed safely!")
    print("Landing speed was " + str(myRocket.getLandingVel()) + " m/s")
else:
  print("The rocket has not yet landed. Try extending the simulation time.")
  
