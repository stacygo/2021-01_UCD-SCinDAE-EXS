# Exercise 2-14: Comparing CDFs

import pandas as pd
import numpy as np
from scipy.stats import norm
import empiricaldist
import matplotlib.pyplot as plt

gss = pd.read_hdf('input/gss.hdf5', 'gss')

# Extract realinc and compute its log
income = gss['realinc']
log_income = np.log10(income)

# Compute mean and standard deviation
mean = np.mean(log_income)
std = np.std(log_income)
print(mean, std)

# Make a norm object
dist = norm(mean, std)

# Evaluate the model CDF
xs = np.linspace(2, 5.5)
ys = dist.cdf(xs)

# Plot the model CDF
plt.clf()
plt.plot(xs, ys, color='gray')

# Create and plot the Cdf of log_income
empiricaldist.Cdf.from_seq(log_income).plot()

# Label the axes
plt.xlabel('log10 of realinc')
plt.ylabel('CDF')
plt.show()
