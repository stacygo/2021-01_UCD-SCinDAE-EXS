# Exercise 3-03: Scatter plot

import pandas as pd
import matplotlib.pyplot as plt

brfss = pd.read_hdf('input/brfss.hdf5', 'brfss')

# Select the first 1000 respondents
brfss = brfss[:1000]

# Extract age and weight
age = brfss['AGE']
weight = brfss['WTKG3']

# Make a scatter plot
plt.plot(age, weight, 'o', markersize=1, alpha=0.1)

plt.xlabel('Age in years')
plt.ylabel('Weight in kg')

plt.show()
