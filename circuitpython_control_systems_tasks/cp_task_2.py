import time
import board
from analogio import AnalogOut

led = AnalogOut(board.A0)

while True:
  for i in range(0, 65535, 64):
        analog_out.value = i
  time.sleep(0.1)
