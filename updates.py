# <main.py>

from machine import Pin
import time
d4 = Pin(2, Pin.OUT)

while True:
  d4.value(not d4.value())
  time.sleep(.5)
