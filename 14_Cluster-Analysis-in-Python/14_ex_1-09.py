# Exercise 1-09: Visualize normalized data

import numpy as np
from matplotlib import pyplot as plt
from scipy.cluster.vq import whiten

goals_for = np.array([4, 3, 2, 3, 1, 1, 2, 0, 1, 4])
scaled_data = whiten(goals_for)

# Plot original data
plt.plot(goals_for, label='original')

# Plot scaled data
plt.plot(scaled_data, label='scaled')

# Show the legend in the plot
plt.legend()

# Display the plot
plt.show()
