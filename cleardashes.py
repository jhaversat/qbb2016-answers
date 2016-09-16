#!/usr/bin/env python

"""removes dashes from homologously aligned sequences"""

import sys

for line in sys.stdin:
    fields = line.rstrip("\r\n").split("\t")
    fields[3] = fields[3].replace("-", "")
    if fields [1] == '1' and fields [2] == '10293':
        print fields [0], fields[3]