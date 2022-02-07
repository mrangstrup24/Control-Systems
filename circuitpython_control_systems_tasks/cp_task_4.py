#same code as cp_task_3.py, as I unknowningly solved this task using previous code
import board
from analogio import AnalogOut, AnalogIn

led = AnalogOut(board.A0)
light_sensor = AnalogIn(board.A1)

while True:
  led.value = (65535/light_sensor.value)
