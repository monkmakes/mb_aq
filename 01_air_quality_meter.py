from microbit import *
import time

def bargraph(a):
    display.clear()
    for y in range(0, 5):
        if a > y:
            for x in range(0, 5):
                display.set_pixel(x, 4-y, 9)

while True:
    e_co2 = pin2.read_analog() * 4
    if button_a.was_pressed():
        display.scroll(e_co2)
    bargraph(e_co2 / 400)
    time.sleep(0.5)