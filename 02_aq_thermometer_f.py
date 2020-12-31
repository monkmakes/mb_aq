from microbit import *
import time

while True:
    temp_c = pin1.read_analog() / 10.23 - 20
    temp_f = int(temp_c * 9 / 5 + 32)
    display.scroll(temp_f)
    time.sleep(0.5)