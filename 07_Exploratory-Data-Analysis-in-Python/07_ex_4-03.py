# Exercise 4-03: Using StatsModels

import pandas as pd
from scipy.stats import linregress
import statsmodels.formula.api as smf

brfss = pd.read_hdf('input/brfss.hdf5', 'brfss')

# Run regression with linregress
subset = brfss.dropna(subset=['INCOME2', '_VEGESU1'])
xs = subset['INCOME2']
ys = subset['_VEGESU1']
res = linregress(xs, ys)
print(res)

# Run regression with StatsModels
results = smf.ols('_VEGESU1 ~ INCOME2', data=brfss).fit()
print(results.params)
