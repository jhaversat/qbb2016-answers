#!/usr/bin/env python

"""when using make sure to take into account that column number 1 will have trailing spaces"""

import sys

for line in sys.stdin:
    if "DROME" in line:
        stringline = line.rstrip("\n")
        print stringline[(len(stringline)-23):(len(stringline)-13)], "\t", stringline[(len(stringline)-11):]
        
        
        
       
    
   
        