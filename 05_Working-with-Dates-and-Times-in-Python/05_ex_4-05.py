# Exercise 4-05: How many joyrides?

import pandas as pd

rides = pd.read_csv('input/capital-onebike.csv', parse_dates=['Start date', 'End date'])

# Subtract the start date from the end date
ride_durations = rides['End date'] - rides['Start date']

# Convert the results to seconds
rides['Duration'] = ride_durations.dt.total_seconds()

# Create joyrides
joyrides = (rides['Start station'] == rides['End station'])

# Total number of joyrides
print("{} rides were joyrides".format(joyrides.sum()))

print(rides['Duration'])
# Median of all rides
print("The median duration overall was {:.2f} seconds"
      .format(rides['Duration'].median()))

# Median of joyrides
print("The median duration for joyrides was {:.2f} seconds"
      .format(rides[joyrides]['Duration'].median()))
