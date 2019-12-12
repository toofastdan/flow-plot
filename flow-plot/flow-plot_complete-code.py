'''Plots scatterplots and heatmaps of protein expression from individual cells from csv files generated by the FlowJo
 software.'''
#______________________________________________________________________________________________________________________#

# Step 1:  Importing the necessary tools for running this analysis.  We need graphics tools:  seaborn and matplotlib.
# We also need to import the CSV module for efficient importing of our large CSV files.  We need pandas to convert
# strings into floats.

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import csv

# Step 2:  Setting up the file path to your CSV files and testing if python can parse them.  Data type should be in
# floats with the exception of the headers

events = pd.read_csv("C:/Users/ToofastDan/flow-plot/flow-plot/FlowJo Sample CSV Files/export_mouse derived MSCs_BM Hx_003_Living.csv")
print(events.head())
print(events.dtypes)

#Step 3:  Setting up the scatterplots using seaborn and matplotlib

# Setting the default styling and colors for the following graphs (I want a white background with no gridlines):
sns.set(style="white")
sns.set_palette("bright")

# Scatterplot for FSC-A vs SSC-A (for control)
f, ax = plt.subplots(figsize=(10,10))
ax = sns.scatterplot(x='FSC-A', y='SSC-A', data=events)
plt.show()

# Scatterplot for FSC-A vs FSC-H (living cells should form a linear line here)
f, ax = plt.subplots(figsize=(10,10))
ax = sns.scatterplot(x='FSC-A', y="FSC-H", data=events)
plt.show()

# Scatterplot for some proteins of interest:
f, ax = plt.subplots(figsize=(10,10))
ax = sns.scatterplot(x='APC-Cy7-A :: TER119-CD45', y='Pacific Blue-A :: CD31', data=events)
plt.show()



# maybe we could write a for loop for every csv file in this folder...
#file = open(events, newline='')       # instructions for how to use the csv module:  (https://www.youtube.com/watch?v=Xi52tx6phRU&t=295s)
#reader = csv.reader(file)


#header = next(reader)       # this skips over the first line in our imported csv files because they contain a header, not numbers
#events = [row for row in reader]    # this reads the remaining lines in the csv files as events - an event corresponds to 1 cell
#events = []
#for column in reader:
#    signal = float(column[1])
#    data.append(signal)


# these lines serve as a test to see if we imported our csv files correctly.
#print(header)
#print(events[0])          # zero order indexing

