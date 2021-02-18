# Exercise 1-06: Tire size constraints

# The pandas package is imported as pd.
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
                             'tire_sizes': ['27']})

# Convert tire_sizes to integer
ride_sharing['tire_sizes'] = ride_sharing['tire_sizes'].astype('int')

# Set all values above 27 to 27
ride_sharing.loc[ride_sharing['tire_sizes'] > 27, 'tire_sizes'] = 27

# Reconvert tire_sizes back to categorical
ride_sharing['tire_sizes'] = ride_sharing['tire_sizes'].astype('category')

# Print tire size description
print(ride_sharing['tire_sizes'].describe())