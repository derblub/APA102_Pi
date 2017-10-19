from apa102 import APA102

"""
Now for the actual rainbow cycle algorithm
"""
try:
    led_count = 432 - 73  # 1/2 Strip plus one LED is broken
    strip = APA102(led_count, brightness=2)  # Low brightness (2 out of max. 31)
    while True:  # Loop forever
        for j in range(led_count << 8):  # Shift the start of the rainbow across the strip
            for i in range(led_count):  # spread (or compress) one rainbow onto the strip
                # For a faster shift, add more than 1 * j per loop (e.g. + 2 * j)
                index = strip.wheel((((i << 8) // led_count) + j * 4) & 255)
                strip.set_pixel_rgb(i, index)
            strip.show()

except KeyboardInterrupt:  # Break...
    print('Interrupted...')
    strip.clear_strip()
    print('Strip cleared')
    strip.cleanup()
    print('SPI closed')
