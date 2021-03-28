# Exercise 1-07: Back to the future

# The datetime package has been imported as dt, alongside all the packages you've been using till now.
import datetime as dt
import pandas as pd

ride_sharing = pd.read_csv('input/ride_sharing_new.csv')
ride_sharing['tire_sizes'] = '27'
ride_sharing['ride_date'] = '2022-01-19'

# Convert ride_date to datetime
ride_sharing['ride_dt'] = pd.to_datetime(ride_sharing['ride_date'])

# Save today's date
today = pd.Timestamp.today()

# Set all in the future to today's date
ride_sharing.loc[ride_sharing['ride_dt'] > today, 'ride_dt'] = today

# Print maximum of ride_dt column
print(ride_sharing['ride_dt'].max())
