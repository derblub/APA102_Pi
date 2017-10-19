#!/usr/bin/env python
from sys import argv
from time import sleep

from apa102 import APA102

if len(argv) > 1:
    pause = float(argv[1])
else:
    pause = 0.01

if len(argv) > 2:
    brightness = int(argv[2])
else:
    brightness = 2

if pause < 0:
    pause = 0
if pause > 10:
    pause = 10

if brightness < 2:
    brightness = 2

if brightness > 31:
    brightness = 31

"""
Chase a segment of LEDs round the strip
"""
try:
    led_count = 432 - 73  # 1/2 Strip plus one LED is broken
    strip = APA102(led_count, brightness)  # Low brightness (2 out of max. 31)
    while True:  # Loop forever
        for j in range(256):  # Change the color through the color wheel
            for q in range(7):
                # For smooth entry and exit, the loop must start and end with hidden pixels
                # This way, the pixels "roll in" and "slide out" of the strip
                for i in range(-5, led_count, 7):  # Each segment is 7 LEDs long
                    index = strip.wheel((i + j) % 255)
                    strip.set_pixel_rgb(i + q, 0)
                    strip.set_pixel_rgb(i + q + 1, 0)
                    strip.set_pixel_rgb(i + q + 2, index)
                    strip.set_pixel_rgb(i + q + 3, index)
                    strip.set_pixel_rgb(i + q + 4, index)
                    strip.set_pixel_rgb(i + q + 5, index)
                    strip.set_pixel_rgb(i + q + 6, index)  # Wrap, if we are at the end of the strip
                strip.show()
                sleep(pause)
except KeyboardInterrupt:  # Break...
    print('Interrupted...')
    strip.clear_strip()
    print('Strip cleared')
    strip.cleanup()
    print('SPI closed')
