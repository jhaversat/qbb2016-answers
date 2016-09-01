#!/usr/bin/env Python
"""
How to run:
    ./homeworkquestion2.py <SRR072893 file>

Generates:
    Histogram of FPKM values for Sample

"""



import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


data = pd.read_table(sys.argv[1])



fpkm_values = data["FPKM"] > 0
fpkm_nonzero = np.log10(data[fpkm_values]["FPKM"])



plt.figure()
plt.hist(fpkm_nonzero, bins = 30)
plt.title("FPKM values for SRR072893")
plt.xlabel("Sample ID")
plt.ylabel("FPKM (abundance)")
#plt.show()
plt.savefig("Day4Homework2.png")
plt.close()