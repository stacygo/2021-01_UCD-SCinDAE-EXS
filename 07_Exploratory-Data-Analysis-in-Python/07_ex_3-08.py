# Exercise 3-08: Income and height

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

brfss = pd.read_hdf('input/brfss.hdf5', 'brfss')

# Drop rows with missing data
data = brfss.dropna(subset=['INCOME2', 'HTM4'])

# Make a violin plot
sns.violinplot(x='INCOME2', y='HTM4', data=data, inner=None)

# Remove unneeded lines and label axes
sns.despine(left=True, bottom=True)
plt.xlabel('Income level')
plt.ylabel('Height in cm')
plt.show()
