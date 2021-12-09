#!/usr/bin/env python3

import sys
i = 0
#airline = None
#code = None
# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = line.split(',')
    # increase counters
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
       #
        # tab-delimited; the trivial word count is 1
    if(i > 0):
        if(words[15] == "1.00" and words[16] != ""):
            print("{0}\t{1}".format(words[16], 1))
    i += 1
