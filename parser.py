#!/usr/bin/env Python

#"""CREATE A CLASS to Parse a single FASTA record from stdin and print it"""

import sys
import fasta
import itertools

#alignedproteins.fa
aminos = sys.stdin
#nodashes.tsv 
nucleotides = open(sys.argv[1])

#aminos
l1 = []
#nucleotides
l2 = []

doc = fasta.FASTAReader(aminos)

for ident, sequence in doc:
    l1.append((ident, sequence))
    
for lines in nucleotides:
    line = lines.rstrip("\r\n").split(" ")
    ident = line[0]
    sequence = line[1]
    l2.append((ident, sequence))
   
for thing in itertools.izip(l2, l1):
    #thing = ((ID, A), (ID, PA))
    nuc_s = thing[0][1]
    pro_s = thing[1][1]
    
    n = 0
    s = ""
    for aa in pro_s:
        if aa == "-":
            s += "---"
        else:
            codon = nuc_s [n:n+3]
            n+=3
            s+=codon        
    print thing[1][0], "\t", s
        
        

