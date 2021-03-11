# Exercise 2-05: Make a CDF

import pandas as pd
import empiricaldist

gss = pd.read_hdf('input/gss.hdf5', 'gss')

# Select the age column
age = gss['age']

# Compute the CDF of age
cdf_age = empiricaldist.Cdf.from_seq(age)

# Calculate the CDF of 30
print(cdf_age(30))
