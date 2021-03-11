# Exercise 3-13: Income and vegetables

import pandas as pd
from scipy.stats import linregress

brfss = pd.read_hdf('input/brfss.hdf5', 'brfss')

# Extract the variables
subset = brfss.dropna(subset=['INCOME2', '_VEGESU1'])
xs = subset['INCOME2']
ys = subset['_VEGESU1']

# Compute the linear regression
res = linregress(xs, ys)
print(res)
