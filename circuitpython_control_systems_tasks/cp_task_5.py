import board
from analogio import AnalogOut, AnalogIn

led = AnalogOut(board.A0)
light_sensor = AnalogIn(board.A1)
led.value = 60000

while True:
  print(light_sensor.value)
