# Exercise 4-11: Linking them together!

# All DataFrames are in your environment, alongside pandas imported as pd.
import pandas as pd
import recordlinkage

restaurants = pd.DataFrame({'rest_name': ['arnie morton  s of chicago'],
                            'rest_addr': ['435 s. la cienega blv .'],
                            'city': ['los angeles'],
                            'phone': [3102461501],
                            'cuisine_type': ['america']})

restaurants_new = pd.DataFrame({'rest_name': ['kokomo'],
                                'rest_addr': ['6333 w. third st.'],
                                'city': ['la'],
                                'phone': [2139330773],
                                'cuisine_type': ['american']})

# Create an indexer and object and find possible pairs
indexer = recordlinkage.Index()

# Block pairing on cuisine_type
indexer.block('cuisine_type')

# Generate pairs
pairs = indexer.index(restaurants, restaurants_new)

# Create a comparison object
comp_cl = recordlinkage.Compare()

# Find exact matches on city, cuisine_types -
comp_cl.exact('city', 'city', label='city')
comp_cl.exact('cuisine_type', 'cuisine_type', label='cuisine_type')

# Find similar matches of rest_name
comp_cl.string('rest_name', 'rest_name', label='name', threshold=0.8)

# Get potential matches and print
potential_matches = comp_cl.compute(pairs, restaurants, restaurants_new)
print(potential_matches)

# Isolate potential matches with row sum >=3
matches = potential_matches[potential_matches.sum(axis=1) >= 3]

# Get values of second column index of matches
matching_indices = matches.index.get_level_values(1)

# Subset restaurants_new based on non-duplicate values
non_dup = restaurants_new[~restaurants_new.index.isin(matching_indices)]

# Append non_dup to restaurants
full_restaurants = restaurants.append(non_dup)
print(full_restaurants)
