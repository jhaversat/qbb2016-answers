#!/usr/bin/env python

import numpy as np
import scipy
from scipy.cluster.hierarchy import dendrogram, linkage
import matplotlib.pylab as plt
import sys

data = open(sys.argv[1])

l1 = []

for line in data.readlines()[1:]:
    fields = line.rstrip("\r\n").split()
    fields[1] = float(fields [1])
    fields [2] = float(fields[2])
    fields [3] = float(fields[3])
    fields [4] = float(fields[4])
    fields [5] = float(fields[5])
    fields [6] = float(fields[6])
    l1.append(fields[1:2])

a = np.array(l1)

linked = linkage(a, 'ward')

plt.figure(figsize=(15, 12))
dendrogram(
            linked,
            orientation='right',
            distance_sort='descending',
            show_leaf_counts=False
          )
plt.savefig("CFU_Poly_dendrogram.png")
#plt.show()


