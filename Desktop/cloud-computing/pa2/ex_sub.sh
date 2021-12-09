#!/bin/bash

CORRECT=0

tmpoutput=`echo -e 5 '\n' 2 | python subtract.py`
f1=`echo $tmpoutput | grep -q -e '2'`
if [ $? = 0 ]; then
    let CORRECT=CORRECT+1
fi

tmpoutput=`echo -e 25 '\n' 20 | python subtract.py`
f1=`echo $tmpoutput | grep -q -e '5'`
if [ $? = 0 ]; then
    let CORRECT=CORRECT+1
fi

exit $CORRECT
