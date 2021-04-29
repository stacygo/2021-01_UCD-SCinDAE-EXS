# Exercise 1-11: FIFA 18: Normalize data

import pandas as pd
from matplotlib import pyplot as plt
from scipy.cluster.vq import whiten

fifa = pd.read_csv('input/fifa_18_sample_data.csv')

# Scale wage and value
fifa['scaled_wage'] = whiten(fifa['eur_wage'])
fifa['scaled_value'] = whiten(fifa['eur_value'])

# Plot the two columns in a scatter plot
fifa.plot(x='scaled_wage', y='scaled_value', kind='scatter')
plt.show()

# Check mean and standard deviation of scaled values
print(fifa[['scaled_wage', 'scaled_value']].describe())
