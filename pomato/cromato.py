#!/usr/bin/env python
import csv
import curses
import sys
import time
from datetime import datetime

from fonts import numbers

try:
    kwargs = {sys.argv[i]: sys.argv[i + 1] for i in range(1, len(sys.argv), 2)}
except IndexError:
    sys.exit(
        "Usage: pomato.py [-s 0] [-f tty-clock]\n"
        "Set any number of options, in any order."
    )

# We're adding the extra seconds just for appearances' sake
work_duration = int(kwargs.get("-s", "0"))*60+1
duration = work_duration
time_format = "%M:%S"
font = kwargs.get("-f", "tty-clock")
messages = {
    0: "'-'",
}


def main(screen):
    global duration
    global finished
    xpad = curses.COLS//2-17
    ypad = curses.LINES//2-2
    screen.keypad(True)

    curses.curs_set(0)

    time.sleep(1)

    while duration:
        duration += 1
        screen.clear()
        # screen.addstr(1, 2, messages[0])
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


def append_to_csv(filename, time):
    # Extracting data
    current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    focus_time = time

    # Appending data to CSV
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = ['current_date', 'focus_time']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Checking if file is empty, if so, write header
        csvfile.seek(0, 2)
        if csvfile.tell() == 0:
            writer.writeheader()

        # Writing data
        writer.writerow({
            'current_date': current_date,
            'focus_time': focus_time
        })


if __name__ == "__main__":
    try:
        curses.wrapper(main)
    except KeyboardInterrupt:
        time_formated = str(time.strftime(time_format, time.gmtime(duration)))
        print("Time Focused:", time_formated)
        append_to_csv('focus.csv', time_formated)
