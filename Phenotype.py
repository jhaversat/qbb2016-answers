#!/usr/bin/env python

import sys

pheno = open(sys.argv[1])

for character in pheno.read()[1:]:
    if character == "_":
        sys.stdout.write(" ")
    else:
        sys.stdout.write(character)    




