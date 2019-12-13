import numpy as np
import pandas as pd

df = pd.DataFrame(events)
df_trimmed = df.iloc[:,2:10]

def mean_calc(df_mean):
    '''function that calculates the mean of each column in the csv file'''
    df_mean = pd.DataFrame([df_trimmed.mean()])
    return(df_mean)