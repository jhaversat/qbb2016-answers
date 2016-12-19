#!/usr/bin/env python

import sys
import matplotlib.pyplot as plt
import pandas as pd
plt.style.use('ggplot')
import numpy as np
import matplotlib.mlab as mlab


freq = open(sys.argv[1])

l1 = []
l2 = []

for line in freq.readlines()[1:]:
    line = line.rstrip("\r\n").split()
    l1.append(float(line[1]))
    l2.append(float(line[4]))

x = l1
y = l2

n, bins, patches = plt.hist(y, bins=50, normed=1, facecolor='blue', alpha=0.75)

plt.xlabel('Frequency of Alternative Allele')
plt.ylabel('Frequency')
plt.title("Allele Frequency Spectrum")
plt.grid(True)
plt.savefig("allelic_frequency_spectrum.png") 
plt.close()
#plt.show()
