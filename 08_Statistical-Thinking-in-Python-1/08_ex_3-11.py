# Exercise 3-11: Plotting the Binomial PMF

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
n_defaults = np.random.binomial(100, 0.05, size=10000)

# Compute bin edges: bins
bins = np.arange(min(n_defaults), max(n_defaults) + 1.5) - 0.5

# Generate histogram
plt.hist(n_defaults, density=True, bins=bins)

# Label axes
plt.xlabel('number of defaults')
plt.ylabel('PMF')

# Show the plot
plt.show()
