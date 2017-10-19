from apa102 import APA102

try:
    strip = APA102(led_count=432)
    head = -9  # Index of first 'on' pixel
    tail = -19  # Index of last 'off' pixel
    color = 0xFF0000  # 'On' color (starts red)

    while True:  # Loop forever

        strip.set_pixel_rgb(head, color)  # Turn on 'head' pixel
        strip.set_pixel_rgb(tail, 0)  # Turn off 'tail'
        strip.show()  # Refresh strip

        head += 1  # Advance head position
        if head >= 432:  # Off end of strip?
            head = 0  # Reset to start
            color >>= 8  # Red->green->blue->black
            if color == 0:
                color = 0xFF0000  # If black, reset to red

        tail += 1  # Advance tail position
        if tail >= 432:
            tail = 0  # Off end? Reset

except KeyboardInterrupt:  # Break...
    print('Interrupted...')
    strip.clear_strip()
    print('Strip cleared')
    strip.cleanup()
    print('SPI closed')
