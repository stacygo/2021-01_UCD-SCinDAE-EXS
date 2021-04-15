# Exercise 4-06: It's getting cold outside, W20529

import pandas as pd

rides = pd.read_csv('input/capital-onebike.csv', parse_dates=['Start date', 'End date'])

# Import matplotlib
import matplotlib.pyplot as plt

# Resample rides to daily, take the size, plot the results
rides.resample('D', on='Start date')\
  .size()\
  .plot(ylim=[0, 15])

# Show the results
plt.show()

# Resample rides to monthly, take the size, plot the results
rides.resample('M', on='Start date')\
  .size()\
  .plot(ylim=[0, 150])

# Show the results
plt.show()
