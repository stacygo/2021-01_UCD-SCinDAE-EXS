# Exercise 3-02: PMF of age

import pandas as pd
import empiricaldist
import matplotlib.pyplot as plt

brfss = pd.read_hdf('input/brfss.hdf5', 'brfss')

# Extract age
age = brfss['AGE']

# Plot the PMF
empiricaldist.Pmf.from_seq(age).bar()

# Label the axes
plt.xlabel('Age in years')
plt.ylabel('PMF')
plt.show()
