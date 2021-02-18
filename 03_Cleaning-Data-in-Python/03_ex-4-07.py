# Exercise 4-07: Pairs of restaurants

# Both DataFrames, pandas and recordlinkage are in your environment.
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
