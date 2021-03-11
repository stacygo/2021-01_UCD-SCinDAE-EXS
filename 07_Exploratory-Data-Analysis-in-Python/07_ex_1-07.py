# Exercise 1-07: Compute a variable

import pandas as pd

nsfg = pd.read_hdf('input/nsfg.hdf5', 'nsfg')

# Select the columns and divide by 100
agecon = nsfg['agecon'] / 100
agepreg = nsfg['agepreg'] / 100

# Compute the difference
preg_length = agepreg - agecon

# Compute summary statistics
print(preg_length.describe())
