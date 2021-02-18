# Exercise 1-03: Numeric data or ... ?

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

# Print the information of ride_sharing
print(ride_sharing.info())

# Print summary statistics of user_type column
print(ride_sharing['user_type'].describe())