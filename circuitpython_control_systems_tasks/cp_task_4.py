import board
from analogio import AnalogOut, AnalogIn

led = AnalogOut(board.A0)
light_sensor = AnalogIn(board.A1)

while True:
  led.value = light_sensor.value
