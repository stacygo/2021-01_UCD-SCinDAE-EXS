# Exercise 2-13: Distribution of income

import pandas as pd
import numpy as np
from scipy.stats import norm

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
