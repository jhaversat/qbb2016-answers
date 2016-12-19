#!/usr/bin/env python

import numpy as np
from pylab import plot, show
from numpy import vstack, array
from numpy.random import rand
from scipy.cluster.vq import kmeans, kmeans2, whiten, vq

import sys

data = open(sys.argv[1])

l1 = []

for line in data.readlines()[1:]:
    fields = line.rstrip("\r\n").split()
    l1.append((float(fields [1]), float(fields [2])))

data = np.array(l1)

# k==2 groups
centroids, idx = kmeans2(data, 2)

plot(data[idx==0,0],data[idx==0,1],'ob',
     data[idx==1,0],data[idx==1,1],'or')
plot(centroids[:,0],centroids[:,1],'sg',markersize=8)











