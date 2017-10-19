import os
from time import clock

import RPi.GPIO as gpio

REBOOT_PIN = 22
thresh = 0.3

gpio.setmode(gpio.BCM)
gpio.setup(REBOOT_PIN, gpio.IN, pull_up_down=gpio.PUD_UP)


def shutdown(channel):
    os.system("sudo shutdown -h now")


def reboot(channel):
    os.system("sudo reboot")


mutt = 0
lastClock = 0


def butt(channel):
    global mutt, lastClock, thresh
    if gpio.input(REBOOT_PIN):
        if mutt == 2:
            print "ignore doubled stop"
            return  # was already stop, so something is fucked up
        else:
            if (clock() - lastClock) > thresh:
                reboot(channel)
            else:
                shutdown(channel)

        mutt = 2  # rising (stop)
    else:
        print "start"
        mutt = 1  # falling (start)
        lastClock = clock()


gpio.add_event_detect(REBOOT_PIN, gpio.BOTH, callback=Butt)
