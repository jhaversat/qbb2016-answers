#!/usr/bin/env Python

"""this code is effective, but there seems to be a small error in the realignment"""

import sys
import fasta
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

homologues = open(sys.argv[1])
query = sys.stdin
#query = sys.argv[2]

codontable = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'*', 'TAG':'*',
    'TGC':'C', 'TGT':'C', 'TGA':'*', 'TGG':'W',
    'YTG':'other',
    }

for ident, sequence in (fasta.FASTAReader(query)):
    qseq = sequence

mutations = {}
#qcount, [ds, dN)]
    
for line in homologues:
    hcount = 0
    qcount = 0
    field = line.rstrip("\r\n").split("\t")
    if len(field[1]) > 10000:
    
        for letter in field [1]:
            hcodon = field[1][hcount:hcount+3]
            qcodon = qseq[qcount:qcount+3]
            if (hcount+3)%3 != 0:
                pass
            else:
                if hcodon == "---":
                    pass
                else:
                    if hcodon == qcodon:
                        qcount +=3
                    else:
                        if len(hcodon) < 3:
                            pass
                        elif len(qcodon) <3 :
                            pass
                        elif hcodon not in codontable:
                            qcount += 3
                            pass
                        elif codontable[hcodon] == codontable[qcodon]:
                            qcount += 3
                            if qcount in mutations:
                                mutations[qcount][0] += 1
                            else:
                                mutations[qcount] = [1,0]
                        else:
                            qcount +=3
                            if qcount in mutations:
                                mutations[qcount][1] += 1
                            else:
                                mutations[qcount] = [0,1]
            hcount += 1
zscore=[]  
keys = []          
for key in mutations:
    zscore.append((mutations[key][0] - mutations[key][1])) 
    keys.append(key)      


a = np.array (zscore)
final = stats.zscore(a)

colors = []
for item in final:
    if item > 3:
        colors.append("red")
    else:
        colors.append("blue")

#plt.figure()
#plt.scatter( x[:,0], x[:,1], c=colors, edgecolor = "none")

plt.figure()
plt.scatter(keys, final, c=colors, edgecolor = "none")
plt.title ("Zscores across homologes")
plt.xlabel("Chromosome Position")
plt.ylabel("Zscore")
    # plt.close()
plt.show()

#final = []
#for key in mutations:
#    final.append((key, final))
    
#print final


#print a
#print zscore
 #   print field[0], hcount, qcount  
#print mutations
#print "done"
            