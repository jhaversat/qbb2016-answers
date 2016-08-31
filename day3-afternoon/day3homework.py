#!/usr/bin/env python

#target --> subset.fa
#query --> the thing they are linking on the assignment
#k = 11

#!/usr/bin/env python

"""
Read sequences from a fasta file, count the number of times each k-mer occurs across all 
sequences and print kmers and counts

usage: day3homework.py k < fasta_file

INPUT YOUR OWN KMER VARIABLE INPUT FOR 'K'
"""

import sys
import fasta

# Command Line arguments
target = open(sys.argv[1])
query = open(sys.argv[2])
k = int ( sys.argv [3] )

kmer_loci = {}

for (ident, sequence) in fasta.FASTAReader(target):
    sequence = sequence.upper()
    for i in range (0, len(sequence)-k):
        kmer = sequence [ i : i+k ]
        if kmer not in kmer_loci:
            kmer_loci [kmer] = [(ident, i)]
        else:
            kmer_loci[kmer].append((ident, i))


for (unknown, code) in fasta.FASTAReader(query):
    for g in range (0, len(code)-k):
        kmer_new = code[ g : g+k ]
        if kmer_new in kmer_loci:
            for ident, pos in kmer_loci[kmer]:
                print ident, pos, g, kmer_new
    #iteritems allows you to return a tuple (key, value) for every key in  a dictionary
    #Hard to use iteritems for sorting soooo....
    

#for kmer in sorted( kmer_counts, key=kmer_counts.get, reverse=True ):
 #   print kmer, kmer_counts[kmer]

#AKA    
#for kmer in kmer_counts:
    #print kmer, kmer_counts[kmer]