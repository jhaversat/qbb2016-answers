#!/usr/bin/env Python
"""
How to run:
    ./homeworkquestion4.py <data1>

Generates:
    a density plot

"""

import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde

data = pd.read_table(sys.argv[1])
f = data["FPKM"]

# 'data' is a 1D array that contains the initial numbers 37231 to 56661
xmin = min(f)
xmax = max(f)   

# get evenly distributed numbers for X axis.
x = np.linspace(xmin, 168, 1000)   # get 1000 points on x axis
nPoints = len(x)

# get actual kernel density.
density = gaussian_kde(f)
y = density(x)

# print the output data
for i in range(nPoints):
    print "%s   %s" % (x[i], y[i])

plt.plot(x, density(x))
plt.savefig("Day4Homework4.png")