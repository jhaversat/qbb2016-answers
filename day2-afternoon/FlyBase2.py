#!/usr/bin/env python

"""Prints the reference gene names from a t_data.ctab file."""

import sys

gene_names_dict = {}

f = open(sys.argv[1])
for line in f:
    value = line.rstrip( "\r\n").split("\t")
    gene_names_dict[value[1]] = value[0]
    
#print gene_names_dict
    
g = open(sys.argv[2])    
for line in g:
    variable = line.rstrip( "\r\n").split("\t")
    if variable[8] in gene_names_dict:
        print variable, gene_names_dict[ variable[8] ]
    else:
        if len(sys.argv) > 3:
            print variable, "x"
        else:
            continue   
    
