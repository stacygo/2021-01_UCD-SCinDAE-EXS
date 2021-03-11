# Exercise 3-07: Distribution of income

import pandas as pd
import empiricaldist
import matplotlib.pyplot as plt

brfss = pd.read_hdf('input/brfss.hdf5', 'brfss')

# Extract income
income = brfss['INCOME2']

# Plot the PMF
empiricaldist.Pmf.from_seq(income).bar()

# Label the axes
plt.xlabel('Income level')
plt.ylabel('PMF')
plt.show()
