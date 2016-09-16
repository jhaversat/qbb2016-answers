#!/usr/bin/env Python

import sys
import fasta
import matplotlib.pyplot as plt
import math

contigs = sys.stdin

contig_count = 0
sequence_length = []

for ident, sequence in (fasta.FASTAReader(contigs)):
    contig_count += 1
    sequence_length.append(len(sequence))
    

print "CONTIG NUMBER:", contig_count
print "MIN:", min(sequence_length)
print "MAX:", max(sequence_length)
print "MEAN:", ((sum(sequence_length))/(len(sequence_length)))
  
total = 0  

for item in reversed(sequence_length):
    if total + item > ((sum(sequence_length))/2):
        print "N50:", item
        break
    else:
        total += item
