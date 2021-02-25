# Exercise 4-06: It's getting cold outside, W20529

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
