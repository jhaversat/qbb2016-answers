#!/usr/bin/env python

import sys


for line in sys.stdin:
    if "DROME" in line:
        stringline = line.rstrip("\n")
        first_space = stringline[(len(stringline)-23):(len(stringline)-13)]
        second = stringline[(len(stringline)-11):]
        print first_space.strip(" "), "\t", second
    