# Exercise 2-03: Finding consistency

# The pandas package has been imported as pd, and the airlines and categories DataFrames are in your environment.
import pandas as pd

airlines = pd.DataFrame({'id': [1351],
                         'day': ['Tuesday'],
                         'airline': ['UNITED INTL'],
                         'destination': ['KANSAI'],
                         'dest_region': ['Asia'],
                         'dest_size': ['Hub'],
                         'boarding_area': ['Gates 91-102'],
                         'dept_time': ['2018-12-31'],
                         'wait_min': [115.0],
                         'cleanliness': ['Clean'],
                         'safety': ['Neutral'],
                         'satisfaction': ['Very satisfied']})

categories = pd.DataFrame({'cleanliness': ['Clean'],
                           'safety': ['Neutral'],
                           'satisfaction': ['Very satisfied']})

# Print categories DataFrame
print(categories)

# Print unique values of survey columns in airlines
print('Cleanliness: ', airlines['cleanliness'].unique(), "\n")
print('Safety: ', airlines['safety'].unique(), "\n")
print('Satisfaction: ', airlines['satisfaction'].unique(), "\n")

# Find the cleanliness category in airlines not in categories
cat_clean = set(airlines['cleanliness']).difference(categories['cleanliness'])

# Find rows with that category
cat_clean_rows = airlines['cleanliness'].isin(cat_clean)

# Print rows with inconsistent category
print(airlines[cat_clean_rows])

# Find the cleanliness category in airlines not in categories
cat_clean = set(airlines['cleanliness']).difference(categories['cleanliness'])

# Find rows with that category
cat_clean_rows = airlines['cleanliness'].isin(cat_clean)

# Print rows with inconsistent category
print(airlines[cat_clean_rows])

# Print rows with consistent categories only
print(airlines[~cat_clean_rows])
