import board
from analogio import AnalogOut, AnalogIn

led = AnalogOut(board.A0)
light_sensor = AnalogIn(board.A1)
led.value = 0
k = 0.1
roomForError = 1000
error = 0

while True:
  error = 30000 - light_sensor.value
  if light_sensor.value > 30000 - roomForError and light_sensor.value < 30000 + roomForError:
    pass
  else:
    led.value += error*k
    
  print(led.value)
    
    
