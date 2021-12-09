#!/usr/bin/env python3

from operator import itemgetter
import sys

def sortLast(val):
    return val[3] 

airline_name = None
air_delay = 0
air_orig = None
air_dest = None
od_count = 1
airline_count = 1
airline = None
# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    airline, origin, dest, delay = line.split('\t', 3)

    # convert count (currently a string) to int
    try:
        delay = int(float(delay))
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if(airline_name == airline and origin == air_orig and dest == air_dest):
        od_count += 1
        air_delay += delay
    else:
        if airline_name:
            # write result to STDOUT
            print("{0}\t{1}\t{2}\t{3}".format(airline_name, air_orig, air_dest, float(air_delay)/od_count))
        air_delay = delay
        airline_name = airline
        air_orig = origin
        air_dest = dest
        od_count = 1

# do not forget to output the last word if needed!
if airline_name == airline and origin == air_orig and dest == air_dest:
    print("{0}\t{1}\t{2}\t{3}".format(airline_name, air_orig, air_dest, float(air_delay)/od_count))
