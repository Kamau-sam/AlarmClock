#!/usr/bin/env python3

from playsound import playsound
import time

CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"

def alarm(seconds):
    time_elapsed = 0

    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1

        time_left = seconds - time_elapsed
        minutes_left = time_left // 60
        seconds_left = time_left % 60

        print(CLEAR_AND_RETURN + f"{minutes_left:02d} : {seconds_left:02d}", end='', flush=True)

    playsound("sound.mp3")

# Set the alarm for 10 seconds as an example
alarm(10)
