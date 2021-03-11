# Exercise 3-10: Computing correlations

import pandas as pd

brfss = pd.read_hdf('input/brfss.hdf5', 'brfss')

# Select columns
columns = ['AGE', 'INCOME2', '_VEGESU1']
subset = brfss[columns]

# Compute the correlation matrix
print(subset.corr())
