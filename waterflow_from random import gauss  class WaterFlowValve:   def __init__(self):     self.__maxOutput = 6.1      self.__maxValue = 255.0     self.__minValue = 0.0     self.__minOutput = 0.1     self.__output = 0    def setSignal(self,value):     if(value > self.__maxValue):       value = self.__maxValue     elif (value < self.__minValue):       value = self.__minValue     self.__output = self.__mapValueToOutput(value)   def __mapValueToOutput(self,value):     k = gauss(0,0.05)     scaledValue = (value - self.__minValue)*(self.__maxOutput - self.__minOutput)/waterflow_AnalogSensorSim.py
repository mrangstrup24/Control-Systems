from random import gauss

class WaterFlowValve:
  def __init__(self):
    self.__maxOutput = 6.1 
    self.__maxValue = 255.0
    self.__minValue = 0.0
    self.__minOutput = 0.1
    self.__output = 0

  def setSignal(self,value):
    if(value > self.__maxValue):
      value = self.__maxValue
    elif (value < self.__minValue):
      value = self.__minValue
    self.__output = self.__mapValueToOutput(value)
  def __mapValueToOutput(self,value):
    k = gauss(0,0.05)
    scaledValue = (value - self.__minValue)*(self.__maxOutput - self.__minOutput)/(self.__maxValue - self.__minValue) + self.__minOutput + k
    return scaledValue
  def getFlowRate(self):
    return self.__output
    
  
