from microbit import *
import time
import music

max_eco2 = 1500

def bargraph(a):
    display.clear()
    for y in range(0, 5):
        if a > y:
            for x in range(0, 5):
                display.set_pixel(x, 4-y, 9)

while True:
    e_co2 = pin2.read_analog() * 4
    bargraph(e_co2 / 400)
    if e_co2 > max_eco2:
        display.show(Image.NO)
        music.pitch(196, 500)
    time.sleep(0.5)
