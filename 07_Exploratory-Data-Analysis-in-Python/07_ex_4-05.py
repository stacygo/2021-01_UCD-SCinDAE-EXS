# Exercise 4-05: Plot income and education

import pandas as pd
import matplotlib.pyplot as plt

gss = pd.read_hdf('input/gss.hdf5', 'gss')

# Group by educ
grouped = gss.groupby('educ')

# Compute mean income in each group
mean_income_by_educ = grouped['realinc'].mean()

# Plot mean income as a scatter plot
plt.plot(mean_income_by_educ, 'o', alpha=0.5)

# Label the axes
plt.xlabel('Education (years)')
plt.ylabel('Income (1986 $)')
plt.show()
