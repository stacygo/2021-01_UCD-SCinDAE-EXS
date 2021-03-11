# Exercise 2-10: Extract education levels

import pandas as pd

gss = pd.read_hdf('input/gss.hdf5', 'gss')

# Select educ
educ = gss['educ']

# Bachelor's degree
bach = (educ >= 16)

# Associate degree
assc = (educ >= 14) & (educ < 16)

# High school (12 or fewer years of education)
high = (educ <= 12)
print(high.mean())
