# Exercise 2-03: Plot a PMF

import pandas as pd
import empiricaldist
import matplotlib.pyplot as plt

gss = pd.read_hdf('input/gss.hdf5', 'gss')

# Select the age column
age = gss['age']

# Make a PMF of age
pmf_age = empiricaldist.Pmf.from_seq(age)

# Plot the PMF
pmf_age.bar(label='age')

# Label the axes
plt.xlabel('Age')
plt.ylabel('PMF')
plt.show()
