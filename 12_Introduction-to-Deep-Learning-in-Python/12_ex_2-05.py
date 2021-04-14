# Exercise 2-05: Scaling up to multiple data points

import numpy as np
from functions import predict_with_network

input_data = [np.array([0, 3]), np.array([1, 2]), np.array([-1, -2]), np.array([4, 0])]

weights_0 = {'output': np.array([1, 1]),
             'node_0': np.array([2, 1]),
             'node_1': np.array([1, 2])}

weights_1 = {'output': np.array([1., 1.5]),
             'node_0': np.array([2, 1]),
             'node_1': np.array([1., 1.5])}

target_actuals = [1, 3, 5, 7]

from sklearn.metrics import mean_squared_error

# Create model_output_0
model_output_0 = []
# Create model_output_1
model_output_1 = []

# Loop over input_data
for row in input_data:
    # Append prediction to model_output_0
    model_output_0.append(predict_with_network(row, weights_0))

    # Append prediction to model_output_1
    model_output_1.append(predict_with_network(row, weights_1))

# Calculate the mean squared error for model_output_0: mse_0
mse_0 = mean_squared_error(target_actuals, model_output_0)

# Calculate the mean squared error for model_output_1: mse_1
mse_1 = mean_squared_error(target_actuals, model_output_1)

# Print mse_0 and mse_1
print("Mean squared error with weights_0: %f" % mse_0)
print("Mean squared error with weights_1: %f" % mse_1)


