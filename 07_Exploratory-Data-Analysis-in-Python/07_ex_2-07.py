# Exercise 2-07:

import pandas as pd
import empiricaldist
import matplotlib.pyplot as plt

gss = pd.read_hdf('input/gss.hdf5', 'gss')

# Select realinc
income = gss['realinc']

# Make the CDF
cdf_income = empiricaldist.Cdf.from_seq(income)

# Plot it
cdf_income.plot()

# Label the axes
plt.xlabel('Income (1986 USD)')
plt.ylabel('CDF')
plt.show()
