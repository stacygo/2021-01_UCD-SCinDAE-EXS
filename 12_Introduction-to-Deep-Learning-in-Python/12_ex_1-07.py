# Exercise 1-07: Applying the network to many observations/rows of data

import numpy as np
from functions import relu, predict_with_network

input_data = [np.array([3, 5]), np.array([1, -1]), np.array([0, 0]), np.array([8, 4])]
weights = {'node_0': np.array([2, 4]),
           'node_1': np.array([4, -5]),
           'output': np.array([2, 7])}

# Create empty list to store prediction results
results = []
for input_data_row in input_data:
    # Append prediction to results
    results.append(predict_with_network(input_data_row, weights))

# Print results
print(results)
