# Step 1:  Importing the necessary tools for running this analysis.  We need graphics tools:  seaborn and matplotlib.
# We also need to import the CSV module for efficient importing of our large CSV files.  We need pandas to convert
# strings into floats.
# Step 2:  Setting up the file path to your CSV files and testing if python can parse them

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import csv

flow_file = pd.read_csv("C:/Users/ToofastDan/flow-plot/flow-plot/FlowJo Sample CSV Files/export_mouse derived MSCs_BM sup Hx_004_Live_dead.csv")
print(flow_file.head())
print(flow_file.dtypes)

test_sns = sns.load_dataset('export_mouse derived MSCs_BM sup Hx_004_Live_dead')
test_sns = test_sns.pivot('FSC-A', 'SSC-A')
display_test_sns = sns.heatmap(test_sns)



# maybe we could write a for loop for every csv file in this folder...
#file = open(flow_file, newline='')       # instructions for how to use the csv module:  (https://www.youtube.com/watch?v=Xi52tx6phRU&t=295s)
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

