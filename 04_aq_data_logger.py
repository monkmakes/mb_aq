from microbit import *
import time

while True:
    e_co2 = pin2.read_analog() * 4
    temp_c = int(pin1.read_analog() / 10.23 - 20)
    print(e_co2)
    time.sleep(1)