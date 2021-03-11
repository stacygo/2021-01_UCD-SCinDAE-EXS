# Exercise 2-11: Plot income CDFs

import pandas as pd
import empiricaldist
import matplotlib.pyplot as plt

gss = pd.read_hdf('input/gss.hdf5', 'gss')

# Select educ
educ = gss['educ']

bach = (educ >= 16)
assc = (educ >= 14) & (educ < 16)
high = (educ <= 12)

income = gss['realinc']

# Plot the CDFs
empiricaldist.Cdf.from_seq(income[high]).plot(label='High school')
empiricaldist.Cdf.from_seq(income[assc]).plot(label='Associate')
empiricaldist.Cdf.from_seq(income[bach]).plot(label='Bachelor')

# Label the axes
plt.xlabel('Income (1986 USD)')
plt.ylabel('CDF')
plt.legend()
plt.show()
