# Exercise 1-04: Summing strings and concatenating numbers

# The pandas package is imported as pd.
import pandas as pd

ride_sharing = pd.DataFrame({'duration': ['12 minutes'],
                             'station_A_id': [81],
                             'station_A_name': ['Berry St at 4th St'],
                             'station_B_id': [323],
                             'station_B_name': ['Broadway at Kearny'],
                             'bike_id': [5480],
                             'user_type': [2],
                             'user_birth_year': [1959],
                             'user_gender': ['Male']})

# Strip duration of minutes
ride_sharing['duration_trim'] = ride_sharing['duration'].str.strip('minutes')

# Convert duration to integer
ride_sharing['duration_time'] = ride_sharing['duration_trim'].astype('int')

# Write an assert statement making sure of conversion
assert ride_sharing['duration_time'].dtype == 'int'

# Print formed columns and calculate average ride duration
print(ride_sharing[['duration','duration_trim','duration_time']])
print(ride_sharing['duration_time'].mean())