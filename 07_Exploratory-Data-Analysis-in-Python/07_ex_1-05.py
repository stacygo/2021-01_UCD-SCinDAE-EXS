# Exercise 1-05: Validate a variable

import pandas as pd

nsfg = pd.read_hdf('input/nsfg.hdf5', 'nsfg')

nsfg['outcome'].value_counts().sort_index()
