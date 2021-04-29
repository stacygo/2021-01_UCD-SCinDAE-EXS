# Exercise 1-08: Normalize basic list data

import numpy as np
from scipy.cluster.vq import whiten

goals_for = np.array([4, 3, 2, 3, 1, 1, 2, 0, 1, 4])

# Use the whiten() function to standardize the data
scaled_data = whiten(goals_for)
print(scaled_data)
