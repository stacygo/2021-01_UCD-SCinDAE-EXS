# Exercise 2-06: Compute IQR

import pandas as pd
import empiricaldist

gss = pd.read_hdf('input/gss.hdf5', 'gss')

cdf_income = empiricaldist.Cdf.from_seq(gss['realinc'])

# Calculate the 75th percentile
percentile_75th = cdf_income.inverse(0.75)
print(percentile_75th)

# Calculate the 25th percentile
percentile_25th = cdf_income.inverse(0.25)
print(percentile_25th)

# Calculate the interquartile range
iqr = percentile_75th - percentile_25th

# Print the interquartile range
print(iqr)
