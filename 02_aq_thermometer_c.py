from microbit import *
import time

while True:
    temp_c = int(pin1.read_analog() / 10.23 - 20)
    display.scroll(temp_c)
    time.sleep(0.5)