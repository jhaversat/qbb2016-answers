#!/usr/bin/env python

import sys
import fasta

Data = open(sys.argv[1])
query = sys.argv[2]
#2 = droYak2_seq.fa

sequential_hits = {}

count = 0
for line in Data:
    fields = line.rstrip("\r\n").split() 
    broken = False
    for key in sequential_hits.keys():
        if fields[0] in key:
            if int(fields[2]) == int(sequential_hits[key][-1])+1: #---> if it's the # plus 1
                sequential_hits[key].append(int(fields[2]))   #--> add that value to the list
                broken = True
                break
    if broken == True:
        pass
    else:                                                     #----> if it's not ajacent
        count += 1
        sequential_hits[fields[0] + str(count)] = [int(fields[2])]

kmers = [] 
for (identifier, hits) in sequential_hits.iteritems():
    for ident, sequence in fasta.FASTAReader(open(query)):
           kmer = sequence[ hits[0] : hits[0] + len(fields[3]) + len(hits) -1]
           kmers.append((len(kmer), identifier, hits[0], kmer))
kmers.sort(reverse=True)
for h in kmers:
    print "ID:", h[1], "| location:", h[2],"| kmer:", h[3], "| kmer length:", h[0]
    