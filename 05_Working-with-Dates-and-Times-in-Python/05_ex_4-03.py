# Exercise 4-03:

import pandas as pd

rides = pd.read_csv('input/capital-onebike.csv', parse_dates=['Start date', 'End date'])

# Subtract the start date from the end date
ride_durations = rides['End date'] - rides['Start date']

# Convert the results to seconds
rides['Duration'] = ride_durations.dt.total_seconds()

print(rides['Duration'].head())
