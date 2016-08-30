#!/usr/bin/env python

import sys

count = 0
number = 0

for line in sys.stdin:
    if line.startswith( "@" ):
        continue
    else:
        if len(line.split("\t")) < 5:
            continue
        else:
            col = line.split( "\t" )[4]
            if col != "255":
                count = count + int(col)
                number = number + 1
print float(count)/number
    
        