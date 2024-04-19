#!/usr/bin/env python
import curses
import os
import sys
import time
from shutil import which

from fonts import numbers

try:
    kwargs = {sys.argv[i]: sys.argv[i + 1] for i in range(1, len(sys.argv), 2)}
except IndexError:
    sys.exit(
        "Usage: pomato.py [-w 25] [-f tty-clock]\n"
        "Set any number of options, in any order."
    )

# We're adding the extra seconds just for appearances' sake
work_duration = int(kwargs.get("-w", "5"))*60+1
duration = work_duration
time_format = "%M:%S"
font = kwargs.get("-f", "tty-clock")


def main(screen):
    global duration
    xpad = curses.COLS//2-17
    ypad = curses.LINES//2-2
    screen.keypad(True)

    curses.curs_set(0)

    while duration:
        duration -= 1
        screen.clear()
        screen.addstr(ypad, 0, draw_timestamp(time.strftime(
            time_format, time.gmtime(duration)), 1, xpad))
        screen.refresh()

        time.sleep(1)


def draw_timestamp(timestamp="00:00", padding=0, lpadding=0):
    global font
    rval = ""
    for i in range(5):
        rval += " "*lpadding
        for character in timestamp:
            if character == ":" and int(timestamp[-1]) % 2 == 1:
                character = " "
            rval += " "*padding + numbers[font][character][i]
        rval += "\n"
    return rval


def alert():
    if which("paplay"):  # Let's not just assume every system has `paplay`
        os.system("paplay " + os.path.dirname(__file__) +
                  os.path.sep + "alert.ogg")


if __name__ == "__main__":
    try:
        curses.wrapper(main)
    except KeyboardInterrupt:
        print("Time left when exiting:", time.strftime(
            time_format, time.gmtime(duration)))
