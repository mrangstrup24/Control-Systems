import board
from analogio import AnalogOut, AnalogIn

led = AnalogOut(board.A0)
light_sensor = AnalogIn(board.A1)
led.value = 60000

while True:
  led.value = 60000-(6000/light_sensor.value)
  print(led.value)
