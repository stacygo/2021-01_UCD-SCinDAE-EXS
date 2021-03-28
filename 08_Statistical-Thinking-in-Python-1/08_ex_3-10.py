# Exercise 3-10: Sampling out of the Binomial distribution

import numpy as np
import matplotlib.pyplot as plt
import functions

np.random.seed(42)

# Take 10,000 samples out of the binomial distribution: n_defaults
n_defaults = np.random.binomial(100, 0.05, size=10000)

# Compute CDF: x, y
x, y = functions.ecdf(n_defaults)

# Plot the CDF with axis labels
plt.plot(x, y, marker='.', linestyle='none')
plt.xlabel('number of defaults')
plt.ylabel('CDF')

# Show the plot
plt.show()
