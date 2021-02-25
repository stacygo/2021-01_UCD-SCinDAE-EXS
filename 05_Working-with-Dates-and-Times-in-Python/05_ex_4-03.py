# Exercise 4-03:

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

# Subtract the start date from the end date
ride_durations = rides['End date'] - rides['Start date']

# Convert the results to seconds
rides['Duration'] = ride_durations.dt.total_seconds()

print(rides['Duration'].head())
