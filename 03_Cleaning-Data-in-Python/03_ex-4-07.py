# Exercise 4-07: Pairs of restaurants

# Both DataFrames, pandas and recordlinkage are in your environment.
import pandas as pd
import recordlinkage

restaurants = pd.read_csv('input/restaurants_L2_dirty.csv')
restaurants_new = pd.read_csv('input/restaurants_L2.csv')

# Create an indexer and object and find possible pairs
indexer = recordlinkage.Index()

# Block pairing on cuisine_type
indexer.block('cuisine_type')

# Generate pairs
pairs = indexer.index(restaurants, restaurants_new)
