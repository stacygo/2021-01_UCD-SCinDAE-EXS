# Exercise 1-07: Back to the future

# The datetime package has been imported as dt, alongside all the packages you've been using till now.
import datetime as dt
import pandas as pd

ride_sharing = pd.DataFrame({'duration': ['12 minutes'],
                             'station_A_id': [81],
                             'station_A_name': ['Berry St at 4th St'],
                             'station_B_id': [323],
                             'station_B_name': ['Broadway at Kearny'],
                             'bike_id': [5480],
                             'user_type': ['Subscriber'],
                             'user_birth_year': [1959],
                             'user_gender': ['Male'],
                             'tire_sizes': ['27'],
                             'ride_date': ['2020-01-19']})

# Convert ride_date to datetime
ride_sharing['ride_dt'] = pd.to_datetime(ride_sharing['ride_date'])

# Save today's date
today = dt.date.today()

# Set all in the future to today's date
ride_sharing.loc[ride_sharing['ride_dt'] > today, 'ride_dt'] = today

# Print maximum of ride_dt column
print(ride_sharing['ride_dt'].max())
