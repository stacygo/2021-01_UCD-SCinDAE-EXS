# Exercise 3-12: A two-sample bootstrap hypothesis test for difference of means

import numpy as np
import functions

force_a = [1.612, 0.605, 0.327, 0.946, 0.541, 1.539, 0.529, 0.628, 1.453, 0.297, 0.703, 0.269,
           0.751, 0.245, 1.182, 0.515, 0.435, 0.383, 0.457, 0.73]

force_b = [0.172, 0.142, 0.037, 0.453, 0.355, 0.022, 0.502, 0.273, 0.72, 0.582, 0.198, 0.198,
           0.597, 0.516, 0.815, 0.402, 0.605, 0.711, 0.614, 0.468]

forces_concat = np.concatenate((force_a, force_b))

# Compute mean of all forces: mean_force
mean_force = np.mean(forces_concat)

# Generate shifted arrays
force_a_shifted = force_a - np.mean(force_a) + mean_force
force_b_shifted = force_b - np.mean(force_b) + mean_force

# Compute 10,000 bootstrap replicates from shifted arrays
bs_replicates_a = functions.draw_bs_reps(force_a_shifted, np.mean, 10000)
bs_replicates_b = functions.draw_bs_reps(force_b_shifted, np.mean, 10000)

# Get replicates of difference of means: bs_replicates
bs_replicates = bs_replicates_a - bs_replicates_b

# Compute and print p-value: p
p = np.sum(bs_replicates >= (np.mean(force_a) - np.mean(force_b))) / 10000
print('p-value =', p)
