# Exercise 4-12: How long between rides?

import pandas as pd

rides = pd.DataFrame({'Start date': ['2017-10-01 15:23:25'],
                      'End date': ['2017-10-01 15:26:26'],
                      'Start station number': [31038],
                      'Start station': ['Glebe Rd & 11th St N'],
                      'End station number': [31036],
                      'End station': ['George Mason Dr & Wilson Blvd'],
                      'Bike number': ['W20529'],
                      'Member type': ['Member']})

rides['Start date'] = pd.to_datetime(rides['Start date'], format="%Y-%m-%d %H:%M:%S")
rides['End date'] = pd.to_datetime(rides['End date'], format="%Y-%m-%d %H:%M:%S")

# Shift the index of the end date up one; now subract it from the start date
rides['Time since'] = rides['Start date'] - (rides['End date'].shift(1))

# Move from a timedelta to a number of seconds, which is easier to work with
rides['Time since'] = rides['Time since'].dt.total_seconds()

# Resample to the month
monthly = rides.resample('M', on='Start date')

# Print the average hours between rides each month
print(monthly['Time since'].mean()/(60*60))
