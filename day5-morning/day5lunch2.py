#!/usr/bin/env python

"""
input:
    ./day5lunch2.py <histone.tab> <t_data.ctab>

use OLS IN STATSMODELS PACKAGE
does the levels of histone modification near my histone start site affect gene expression?
take histone start site (putative tss region --> written chrom /t start/t and /t ___), expand it out by 500
bigwigaverageoverbed will give you a file that has the average signal for each of those histone modifications
combine that with your FPKMs (file for each transcript --> each histone signal and the corresponding FPKMs)
do regression using statsmodels formula osl()
(using chipseq data) - if for real would want chipseq and rnaseq data on the same sample
output --> 4 regression sequences
    can tell the p value associated with the coefficients
    R2 of the coefficient
    magnitude of the Beta1

"""

import sys
import pandas as pd
import statsmodels.api as sm
import numpy as np

histone = pd.read_table(sys.argv[1])
fpkm = pd.read_table(sys.argv[2])

d = {}
for i in histone.itertuples():
    name = i[1]
    signal = i[6]
    d[name] = [signal]

for i in fpkm.itertuples():
    name = i[6]
    fpkm = i[-1]
    if name in d:
        d[name].append([fpkm])

signal_lst = []
fpkm_lst = []

for key in d.keys():
    signal = d[key][0]
    fpkm = d[key][1]
    signal_lst.append(signal)
    fpkm_lst.append(fpkm)

Y = signal_lst
X = fpkm_lst


model = sm.OLS(Y,X)
results = model.fit()
print results.summary()


#results.params 
#array([ 2.14285714, 0.25])
#results.tvalues
#array([ 1.87867287,  0.98019606])
#print(results.t_test([1, 0]))
#<T test: effect=array([ 2.14285714]), sd=array([[ 1.14062282]]), t=array([[ 1.87867287]]), p=array([[ 0.05953974]]), df_denom=5>
#print(results.f_test(np.identity(2)))
#<F test: F=array([[ 19.46078431]]), p=[[ 0.00437251]], df_denom=5, df_num=2>