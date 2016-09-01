#!/usr/bin/env Python
"""
How to run:
    ./homeworkquestion3.py <Sample1.ctab> <Sample2.ctab

Generates:
    a MA plot logging FPKA values of samples(different developmental stages) against one another
   

"""

import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data1 = pd.read_table(sys.argv[1])
data2 = pd.read_table(sys.argv[2])

fpkm1 = data1["FPKM"]+1
fpkm2 = data2["FPKM"]+1

m = np.log2((fpkm1/fpkm2))
a = (np.log2((fpkm1*fpkm2)))/2


plt.figure()
plt.scatter(a, m)
plt.title("FPKM values for SRR072893 and SRR072915")
plt.xlabel("FPKM Sample 1")
plt.ylabel("FPKM Sample 2")
#plt.show()
plt.savefig("Day4Homework3.png")
plt.close()