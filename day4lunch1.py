#!/usr/bin/env python

import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_table( sys.argv[1] )
df2 = pd.read_table( sys.argv[2] )

df_roi = df[ "gene_name" ] == "Sxl"
df_Sxl = df [ df_roi ]
df2_roi = df2[ "gene_name" ] == "Sxl"
df2_Sxl = df2 [ df2_roi ]


df_values = df_Sxl[ "FPKM" ] > 0
df_SxlFPKM = df_Sxl[ df_values ]
df2_values = df2_Sxl[ "FPKM" ] > 0
df2_SxlFPKM = df2_Sxl[ df2_values ]

x1 = np.log10(df_SxlFPKM["FPKM"])
x2 = np.log10(df2_SxlFPKM["FPKM"])
stage = ["stage1", "stage2"]
#============================================================#
# LOAD SOME DATA TO USE

plt.figure()                       # Open a blank canvas
plt.title("Sxl Transcript Abundance") # Add a title to the top

plt.boxplot([x1, x2], labels = stage)
plt.xlabel("Developmental stage")              # Label the x-axis
plt.ylabel("log(FPKM)")       # Label the y-axis with the first feature name
plt.savefig("Boxplot1.png")   # Save the plot
plt.close()                        # Close the canvas



#labels = ["Sepal Length", "Sepal Width", "Petal Length", "Petal Width",]
#species = ["Setosa", "Versicolour", "Virginica"]



#plt.figure()
#plt.plot()
#plt.title (" ")
#plt.savefig("smoothie.png")
#plt.close


#Merged = pd.merge (df_SxlFPKM, df2_SxlFPKM, on = "t_name")
#print Merged




#rolling is the function that gives us the rolling average
#smoothie = df_chrom[ "FPKM" ].rolling(200).mean()
    #200, then the next 200, then the next 200 (like continuous kamers)...
    #calculate a mean for every step of x + 200







    