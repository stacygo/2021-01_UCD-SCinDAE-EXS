# Exercise 1-11: Treating duplicates

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

# Drop complete duplicates from ride_sharing
ride_dup = ride_sharing.drop_duplicates()

# Create statistics dictionary for aggregation function
statistics = {'user_birth_year': 'min', 'duration': 'mean'}

# Group by ride_id and compute new statistics
ride_unique = ride_dup.groupby('ride_id').agg(statistics).reset_index()

# Find duplicated values again
duplicates = ride_unique.duplicated(subset='ride_id', keep=False)
duplicated_rides = ride_unique[duplicates]

# Assert duplicates are processed
assert duplicated_rides.shape[0] == 0
