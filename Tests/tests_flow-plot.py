import numpy as np
import pandas as pd

events = pd.read_csv("C:/Users/ToofastDan/flow-plot/flow-plot/FlowJo Sample CSV Files/export_mouse derived MSCs_BM adh Hx_005_Live_dead.csv")
for column in events:
    assert events[column].dtypes == np.float64