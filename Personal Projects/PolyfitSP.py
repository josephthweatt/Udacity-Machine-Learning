#!/usr/bin/python
#get data from s&p 500, then fit a model to it, and then print as graph

#extract data
import pandas as pd
in_file = "table.csv"
all_data = pd.read_csv(in_file)

import numpy as np
import matplotlib.dates as dates 
import matplotlib.pyplot as plt
dates = map(lambda x: dates.datestr2num(x), all_data['Date'].tolist())
closes = map(lambda x: int(x), all_data['Close'].tolist())
coeffs = np.polyfit(dates, closes, 10)
function = np.poly1d(coeffs)
plt.plot(dates, function(dates))
plt.plot(dates, closes)
plt.show()