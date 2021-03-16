# Exercise 1-07: Adjusting the number of bins in a histogram

import matplotlib.pyplot as plt

versicolor_petal_length = [4.7, 4.5, 4.9, 4.,  4.6, 4.5, 4.7, 3.3, 4.6, 3.9, 3.5, 4.2, 4., 4.7,
                           3.6, 4.4, 4.5, 4.1, 4.5, 3.9, 4.8, 4., 4.9, 4.7, 4.3, 4.4, 4.8, 5.,
                           4.5, 3.5, 3.8, 3.7, 3.9, 5.1, 4.5, 4.5, 4.7, 4.4, 4.1, 4., 4.4, 4.6,
                           4., 3.3, 4.2, 4.2, 4.2, 4.3, 3., 4.1]

# Import numpy
import numpy as np

# Compute number of data points: n_data
n_data = len(versicolor_petal_length)

# Number of bins is the square root of number of data points: n_bins
n_bins = np.sqrt(n_data)

# Convert number of bins to integer: n_bins
n_bins = int(n_bins)

# Plot the histogram
_ = plt.hist(versicolor_petal_length, bins=n_bins)

# Label axes
_ = plt.xlabel('petal length (cm)')
_ = plt.ylabel('count')

# Show histogram
plt.show()
