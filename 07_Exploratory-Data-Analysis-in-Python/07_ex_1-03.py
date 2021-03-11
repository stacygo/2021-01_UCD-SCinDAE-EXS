# Exercise 1-03: Exploring the NSFG data

import pandas as pd

nsfg = pd.read_hdf('input/nsfg.hdf5', 'nsfg')

# Display the number of rows and columns
nsfg.shape

# Display the names of the columns
nsfg.columns

# Select column birthwgt_oz1: ounces
ounces = nsfg['birthwgt_oz1']

# Print the first 5 elements of ounces
print(ounces.head())
