# Exercise 3-06: Height and weight

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

brfss = pd.read_hdf('input/brfss.hdf5', 'brfss')

# Drop rows with missing data
data = brfss.dropna(subset=['_HTMG10', 'WTKG3'])

# Make a box plot
sns.boxplot(x='_HTMG10', y='WTKG3', data=data, whis=10)

# Plot the y-axis on a log scale
plt.yscale('log')

# Remove unneeded lines and label axes
sns.despine(left=True, bottom=True)
plt.xlabel('Height in cm')
plt.ylabel('Weight in kg')
plt.show()
