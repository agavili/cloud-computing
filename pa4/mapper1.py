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
        #print("{0}\t".format(word))
    if(words[14] != ""):
        arr_delay = words[14]
        airline = words[1]
    if(i > 0):
        print("{0}\t{1}".format(airline, arr_delay))
    i += 1
