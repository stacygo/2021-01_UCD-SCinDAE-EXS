# Exercise 4-03: The cutoff point

import pandas as pd

restaurants = pd.DataFrame({'rest_name': ['arnie morton  s of chicago'],
                            'rest_addr': ['435 s. la cienega blv .'],
                            'city': ['los angeles'],
                            'phone': [3102461501],
                            'cuisine_type': ['america']})

# Import process from fuzzywuzzy
from fuzzywuzzy import process

# Store the unique values of cuisine_type in unique_types
unique_types = restaurants['cuisine_type'].unique()

# Calculate similarity of 'asian' to all values of unique_types
print(process.extract('asian', unique_types, limit=len(unique_types)))

# Calculate similarity of 'american' to all values of unique_types
print(process.extract('american', unique_types, limit=len(unique_types)))

# Calculate similarity of 'italian' to all values of unique_types
print(process.extract('italian', unique_types, limit=len(unique_types)))