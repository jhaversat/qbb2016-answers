#!/usr/bin/env python

"""
Command line prompt:
./___.py Sample1.ctab Sample2.ctab Rolling_avg_Window_size
"""

import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df1 = pd.read_table( sys.argv[1] )
df2 = pd.read_table( sys.argv[2] )
window_size = sys.argv[3]


def blender(chr, data_frame, window_size):
    df = data_frame
    df_roi = df["chr"] == "%s" % (chr)
    df_chrom = df[df_roi]
    smoothie = df_chrom["FPKM"].rolling(window_size).mean()
    return smoothie


chr_list = ['2L', '2R', '3L', '3R', '4', 'X']

for i in chr_list:
    smoothie1 = blender(i, df1, int(window_size))
    smoothie2 = blender(i, df2, int(window_size))
    
    plt.figure()
    plt.plot(smoothie1, label = "893")
    plt.plot(smoothie2, label = "915")
    plt.title("Chromosome %s, FPKM rolling mean (size %s)" % (i, str(window_size)))
    plt.xlabel("Relative Position")
    plt.ylabel("FPKM Mean")
    plt.legend(loc="upper right")
    plt.savefig("chr_%s.png" % (i))
    plt.close()