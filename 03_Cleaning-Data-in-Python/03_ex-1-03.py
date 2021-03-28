# Exercise 1-03: Numeric data or ... ?

# The pandas package is imported as pd.
import pandas as pd

ride_sharing = pd.read_csv('input/ride_sharing_new.csv')

# Print the information of ride_sharing
print(ride_sharing.info())

# Print summary statistics of user_type column
print(ride_sharing['user_type'].describe())
