# Exercise 1-11: Treating duplicates

# A sample of ride_sharing is in your environment, as well as all the packages you've been working with thus far.
import pandas as pd

ride_sharing = pd.read_csv('input/ride_sharing_new.csv')
ride_sharing['tire_sizes'] = '27'
ride_sharing['ride_date'] = '2018-03-04'

ride_sharing['duration_trim'] = ride_sharing['duration'].str.strip('minutes')
ride_sharing['duration_time'] = ride_sharing['duration_trim'].astype('int')

# Drop complete duplicates from ride_sharing
ride_dup = ride_sharing.drop_duplicates()

# Create statistics dictionary for aggregation function
statistics = {'user_birth_year': 'min', 'duration_time': 'mean'}

# Group by ride_id and compute new statistics
ride_unique = ride_dup.groupby('ride_id').agg(statistics).reset_index()

# Find duplicated values again
duplicates = ride_unique.duplicated(subset='ride_id', keep=False)
duplicated_rides = ride_unique[duplicates]

# Assert duplicates are processed
assert duplicated_rides.shape[0] == 0
