from random import random
import board
import random
import neopixel
import time
from analogio import AnalogOut

BRIGHTNESS = 0.6

pixel = neopixel.NeoPixel(board.A3, 10, brightness=BRIGHTNESS, auto_write=False)
analog_out = AnalogOut(board.A0)
colors = ["red", "blue", "green", "yellow", "teal", "white", "purple"]

def fill_color(intensity, color):
    rgb = [0, 0, 0]

    if colors[color] == "red" or colors[color] == "yellow" or colors[color] == "white" or colors[color] == "purple":
        rgb[0] = intensity

    if colors[color] == "yellow" or colors[color] == "white" or colors[color] == "green" or colors[color] == "teal":
        rgb[1] = intensity

    if colors[color] == "white" or colors[color] == "purple" or colors[color] == "blue" or colors[color] == "teal":
        rgb[2] = intensity

    pixel.fill(rgb)
    pixel.write()

def cycle_lfo(cycle_interval_sleep, color):
    finished = False
    intensity = 0
    increment = 5

    while not finished:
        intensity += increment

        if intensity >=255:
            intensity = 255
            increment = -5

        if intensity <= 0:
            intensity = 0
            finished = True

        analog_out.value = intensity * 255
        fill_color(intensity, color)
        time.sleep(cycle_interval_sleep)

while True:
    cycle_interval_sleep = random.randint(1, 50) * .001
    color = random.randint(0, 6)
    cycle_lfo(cycle_interval_sleep, color)

    # Sleep from half a second to 6.5 seconds
    time_to_sleep = (random.random() * 6) + 0.5
    time.sleep(time_to_sleep)