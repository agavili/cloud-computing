#!/usr/bin/env python3

import sys

i = 0
# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = line.split(',')
    
    # increase counters
#    for word in words:
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1
    if(words[14] != "" and words[4] != "" and words[9] != ""):
        arr_delay = words[14]
        origin = words[4]
        dest = words[9]
        airline = words[1]
    if(i > 0):
        if((airline == "\"B6\"" or airline == "\"G4\"" or airline == "\"MQ\"")):
            print("{0}\t{1}\t{2}\t{3}".format(airline, origin, dest, arr_delay))
    i += 1
