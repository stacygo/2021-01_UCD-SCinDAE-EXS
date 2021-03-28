# Exercise 4-06: The Normal CDF

import numpy as np
import matplotlib.pyplot as plt
import functions

samples_std1 = np.random.normal(20, 1, size=100000)
samples_std3 = np.random.normal(20, 3, size=100000)
samples_std10 = np.random.normal(20, 10, size=100000)

# Generate CDFs
x_std1, y_std1 = functions.ecdf(samples_std1)
x_std3, y_std3 = functions.ecdf(samples_std3)
x_std10, y_std10 = functions.ecdf(samples_std10)

# Plot CDFs
plt.plot(x_std1, y_std1, marker='.', linestyle='none')
plt.plot(x_std3, y_std3, marker='.', linestyle='none')
plt.plot(x_std10, y_std10, marker='.', linestyle='none')

# Make a legend and show the plot
_ = plt.legend(('std = 1', 'std = 3', 'std = 10'), loc='lower right')
plt.show()
