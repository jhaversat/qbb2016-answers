#!/usr/bin/env Python
"""
How to run:
    ./homeworkquestion1.py  <metadata.csv>  <ctab_dir>

Generates:
    Line plot of 

"""



import sys
import pandas as pd
import matplotlib.pyplot as plt

Sample_file = pd.read_csv(sys.argv[1])
replicate_file = pd.read_csv(sys.argv[2])
ctab_dir = sys.argv[3]

female_Sxl = []
male_Sxl = []
female_reps = []
male_reps = []

female_samples2 = replicate_file["sex"] == "female"
for sample in replicate_file[ female_samples2 ]["sample"] :
    filename = ctab_dir + "/" + sample + "/t_data.ctab"
    df = pd.read_table(filename)
    
    Sxl_samples = df[ "t_name"] == "FBtr0331261"
    #print type(df[df_roi2]["FPKM"].values)
    female_reps.append(df[Sxl_samples]["FPKM"].values)
    #.values returns just a number without all the fancy wrapping

female_samples = Sample_file["sex"] == "female"
for sample in Sample_file[ female_samples ]["sample"] :
    filename = ctab_dir + "/" + sample + "/t_data.ctab"
    df = pd.read_table(filename)
    
    Sxl_samples = df[ "t_name"] == "FBtr0331261"
    #print type(df[df_roi2]["FPKM"].values)
    female_Sxl.append(df[Sxl_samples]["FPKM"].values)
    #.values returns just a number without all the fancy wrapping

dev_stage = (Sample_file[female_samples]["stage"].values)

male_samples = Sample_file["sex"] == "male"
for sample in Sample_file[ male_samples ]["sample"] :
    filename = ctab_dir + "/" + sample + "/t_data.ctab"
    df = pd.read_table(filename)
    
    Sxl_samples = df[ "t_name"] == "FBtr0331261"
    #print type(df[df_roi2]["FPKM"].values)
    male_Sxl.append(df[Sxl_samples]["FPKM"].values)
    #.values returns just a number without all the fancy wrapping
    
male_samples2 = replicate_file["sex"] == "male"
for sample in replicate_file[ male_samples2 ]["sample"] :
    filename = ctab_dir + "/" + sample + "/t_data.ctab"
    df = pd.read_table(filename)
    
    Sxl_samples = df[ "t_name"] == "FBtr0331261"
    #print type(df[df_roi2]["FPKM"].values)
    male_reps.append(df[Sxl_samples]["FPKM"].values)
    #.values returns just a number without all the fancy wrapping


Replica = [4, 5, 6, 7]



plt.figure()
plt.plot(female_Sxl, color = 'r')
plt.plot(male_Sxl)
plt.scatter(Replica, female_reps, color = 'r')
plt.scatter(Replica, male_reps)

plt.title("Sxl abundance by developmental stage")
plt.xticks( range(len(dev_stage)), dev_stage)
plt.xlabel("developmental stage (days)")
plt.ylabel("FPKM (abundance)")
#plt.show()
plt.savefig("Day4Homework1.png")
plt.close()