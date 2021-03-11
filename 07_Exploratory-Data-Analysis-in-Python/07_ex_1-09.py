# Exercise 1-09: Make a histogram

import pandas as pd
import matplotlib.pyplot as plt

nsfg = pd.read_hdf('input/nsfg.hdf5', 'nsfg')

# Select the columns and divide by 100
agecon = nsfg['agecon'] / 100

# Plot the histogram
plt.hist(agecon.dropna(), bins=20, histtype='step')

# Label the axes
plt.xlabel('Age at conception')
plt.ylabel('Number of pregnancies')

# Show the figure
plt.show()
