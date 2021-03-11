# Exercise 1-06: Clean a variable

import pandas as pd
import numpy as np

nsfg = pd.read_hdf('input/nsfg.hdf5', 'nsfg')

# Replace the value 8 with NaN
nsfg['nbrnaliv'].replace([8], np.nan, inplace=True)

# Print the values and their frequencies
print(nsfg['nbrnaliv'].value_counts())
