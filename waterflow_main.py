from AnalogSensorSim import WaterFlowValve

myWaterValve = WaterFlowValve()
currentValue = 0.0


#Your task is to send the valve a correct signal to get the flow rate to be 4.5 L/s.

currentTime = 0.0
currentSignal = 0
setpoint = 4.5

k = 10
kA = 0.1
output = 0
sum_error = 0
tolerance = 0.001
change = True

while(currentTime < 10.0):
  valveFlowSensorValue = myWaterValve.getFlowRate()
  
  
  if(change):
    error = setpoint - myWaterValve.getFlowRate()
    sum_error += error
    output += k*error
    myWaterValve.setSignal(output)
    

  if(myWaterValve.getFlowRate()+tolerance > setpoint and myWaterValve.getFlowRate()-tolerance < setpoint):
    change = False
  
  output += kA*error
  print(currentTime,",",valveFlowSensorValue)
  currentTime += 0.1
print(change)
print(myWaterValve.getFlowRate()+tolerance > setpoint and myWaterValve.getFlowRate()-tolerance < setpoint)
