import board
from analogio import AnalogOut, AnalogIn
import time

led = AnalogOut(board.A0)
light_sensor = AnalogIn(board.A1)
led.value = 0
k = 0.1
roomForError = 1000
error = 0

while True:
  error = 30000 - light_sensor.value
  if abs(error) < roomForError:
    pass
  else:
    led.value -= error*k
    
  print(led.value)
  time.sleep(0.1)
    
    
