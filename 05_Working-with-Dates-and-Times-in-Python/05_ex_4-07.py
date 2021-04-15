# Exercise 4-07: Members vs casual riders over time

import pandas as pd

rides = pd.read_csv('input/capital-onebike.csv', parse_dates=['Start date', 'End date'])

# Resample rides to be monthly on the basis of Start date
monthly_rides = rides.resample('M', on='Start date')['Member type']

# Take the ratio of the .value_counts() over the total number of rides
print(monthly_rides.value_counts() / monthly_rides.size())
