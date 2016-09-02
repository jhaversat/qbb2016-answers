#!/usr/bin/env python

"""
use OLS IN STATSMODELS PACKAGE
does the levels of histone modification near my histone start site affect gene expression?
take histone start site (putative tss region --> written chrom /t start/t and /t ___), expand it out by some number of 
bigwigaverageoverbed will give you a file that has the average signal fo each of those histone modifications
combine that with your FPKMs (file with for each transcript --> each histone signal and the corresponding FPKMs)
do regression using statsmodels formula osl()
(using chipseq data) - if for real would want chipseq and rnaseq data on the same sample
output --> 4 regression sequences
    can tell the p value associated with the coefficients
    R2 of the coefficient
    magnitude of the Beta1

"""

import sys
import pandas as pd

base = sys.argv[1]


df = pd.read_table(sys.argv[1])
 
lst = []

for i in df.itertuples():
    chrom = i[2]
    if chrom in ["2L" , "2R" , "3L" , "3R" , "4" , "X", "Y"]:
        t_name = i[6]
        if i[3] == "+":
            start = int(i[4]) - 500
            end = int(i[4]) + 500
            lst.append ((chrom, start, end, t_name))
        elif i[3] == "-":
            start = int(i[5]) + 500
            end = int(i[5]) - 500
            lst.append ((chrom, start, end, t_name))

df = pd.DataFrame( lst )
df.columns = ['Chrom', 'Start', 'End', 't_name']
df.to_csv("Day5lunch1.bed", sep ="\t", index = None)

