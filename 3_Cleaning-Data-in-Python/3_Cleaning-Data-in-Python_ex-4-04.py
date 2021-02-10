# Exercise 4-04: Remapping categories II

# The restaurants DataFrame is in your environment, and
# you have access to a categories list containing the correct cuisine types
# ('italian', 'asian', and 'american').

import pandas as pd
from fuzzywuzzy import process

restaurants = pd.DataFrame({'rest_name': ['arnie morton  s of chicago'],
                            'rest_addr': ['435 s. la cienega blv .'],
                            'city': ['los angeles'],
                            'phone': [3102461501],
                            'cuisine_type': ['america']})

categories = ['italian', 'asian', 'american']

# Inspect the unique values of the cuisine_type column
print(restaurants['cuisine_type'].unique())

# Create a list of matches, comparing 'italian' with the cuisine_type column
matches = process.extract('italian', restaurants['cuisine_type'], limit=len(restaurants['cuisine_type']))

# Inspect the first 5 matches
print(matches[0:5])

# Create a list of matches, comparing 'italian' with the cuisine_type column
matches = process.extract('italian', restaurants['cuisine_type'], limit=len(restaurants.cuisine_type))

# Iterate through the list of matches to italian
for match in matches:
    # Check whether the similarity score is greater than or equal to 80
    if match[1] >= 80:
        # Select all rows where the cuisine_type is spelled this way, and set them to the correct cuisine
        restaurants.loc[restaurants['cuisine_type'] == match[0], 'cuisine_type'] = 'italian'

# Iterate through categories
for cuisine in categories:
    # Create a list of matches, comparing cuisine with the cuisine_type column
    matches = process.extract(cuisine, restaurants['cuisine_type'], limit=len(restaurants.cuisine_type))

    # Iterate through the list of matches
    for match in matches:
        # Check whether the similarity score is greater than or equal to 80
        if match[1] >= 80:
            # If it is, select all rows where the cuisine_type is spelled this way, and set them to the correct cuisine
            restaurants.loc[restaurants['cuisine_type'] == match[0]] = cuisine

# Inspect the final result
restaurants['cuisine_type'].unique()
