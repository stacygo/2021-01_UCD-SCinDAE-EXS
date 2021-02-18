# Exercise 1-10: Finding duplicates

# A sample of ride_sharing is in your environment, as well as all the packages you've been working with thus far.
import pandas as pd

ride_sharing = pd.DataFrame({'ride_id': [0],
                             'duration': [11],
                             'station_A_id': [16],
                             'station_A_name': ['Steuart St at Market St'],
                             'station_B_id': [93],
                             'station_B_name': ['4th St at Mission Bay Blvd S'],
                             'bike_id': [5504],
                             'user_type': ['Subscriber'],
                             'user_birth_year': [1988],
                             'user_gender': ['Male'],
                             'tire_sizes': ['27'],
                             'ride_date': ['2018-03-04']})

# Find duplicates
duplicates = ride_sharing.duplicated(subset='ride_id', keep=False)

# Sort your duplicated rides
duplicated_rides = ride_sharing[duplicates].sort_values(by='ride_id')

# Print relevant columns of duplicated_rides
print(duplicated_rides[['ride_id', 'duration', 'user_birth_year']])
