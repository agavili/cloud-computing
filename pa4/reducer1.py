#!/usr/bin/env python3

from operator import itemgetter
import sys

airline_name = None
air_delay = 0
airline_count = 1
airline = None

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    airline, delay = line.split('\t', 1)

    # convert count (currently a string) to int
    try:
        delay = int(float(delay))
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if airline_name == airline:
        airline_count += 1
        air_delay += delay
    else:
        if airline_name:
            # write result to STDOUT
            print("{0}\t{1}".format(airline_name, float(air_delay)/airline_count))
        air_delay = delay
        airline_name = airline
        airline_count = 1

# do not forget to output the last word if needed!
if airline_name == airline:
    print("{0}\t{1}".format(airline_name, float(air_delay)/airline_count))
