#!/usr/bin/env python

import sys
import matplotlib.pyplot as plt
import pandas as pd
plt.style.use('ggplot')
import numpy as np


eigenvec = open(sys.argv[1])


#labels = ["Sepal Length", "Sepal Width", "Petal Length", "Petal Width",]
#species = ["Setosa", "Versicolour", "Virginica"]

#============================================================#
# CREATE SOME PLOTS

l1 = []
l2 = []

eigenvec_list = eigenvec.readlines()

line1 = eigenvec_list[0:1]
line2 = eigenvec_list[1:2]

# Extract two features from the data to plot
for line in line1:
    line = line.rstrip("\r\n").split(" ")
    l1.extend(line[2:])
    
for i, item in enumerate(l1):
    l1[i] = float(item)
    
for line in line2:
    line = line.rstrip("\r\n").split(" ")
    l2.extend(line[2:])
    
for i, item in enumerate(l2):
    l2[i] = float(item)
    

x = l1
y = l2

plt.figure()  
plt.title("Principle Component Analysis")                    # Create a blank canvas
plt.scatter(x,y)                 # Plot x vs y as points
plt.xlabel("A01 01")                 # label the x-axis
plt.ylabel("A01 02")                 # label the y-axis
plt.savefig("Principle_Component_Analysis_Plot.png") # Save the figure
plt.close()                      # Close the canvas
#plt.show()

