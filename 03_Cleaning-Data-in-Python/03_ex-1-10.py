# Exercise 1-10: Finding duplicates

# A sample of ride_sharing is in your environment, as well as all the packages you've been working with thus far.
import pandas as pd

ride_sharing = pd.read_csv('input/ride_sharing_new.csv')
ride_sharing['tire_sizes'] = '27'
ride_sharing['ride_date'] = '2018-03-04'

# Find duplicates
duplicates = ride_sharing.duplicated(subset='ride_id', keep=False)

# Sort your duplicated rides
duplicated_rides = ride_sharing[duplicates].sort_values(by='ride_id')

# Print relevant columns of duplicated_rides
print(duplicated_rides[['ride_id', 'duration', 'user_birth_year']])
