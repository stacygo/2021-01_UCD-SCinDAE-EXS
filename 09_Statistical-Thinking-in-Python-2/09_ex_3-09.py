# Exercise 3-09: Permutation test on frog data

import numpy as np
import functions

force_a = [1.612, 0.605, 0.327, 0.946, 0.541, 1.539, 0.529, 0.628, 1.453, 0.297, 0.703, 0.269,
           0.751, 0.245, 1.182, 0.515, 0.435, 0.383, 0.457, 0.73]

force_b = [0.172, 0.142, 0.037, 0.453, 0.355, 0.022, 0.502, 0.273, 0.72, 0.582, 0.198, 0.198,
           0.597, 0.516, 0.815, 0.402, 0.605, 0.711, 0.614, 0.468]

# Compute difference of mean impact force from experiment: empirical_diff_means
empirical_diff_means = functions.diff_of_means(force_a, force_b)

# Draw 10,000 permutation replicates: perm_replicates
perm_replicates = functions.draw_perm_reps(force_a, force_b, functions.diff_of_means, size=10000)

# Compute p-value: p
p = np.sum(perm_replicates >= empirical_diff_means) / len(perm_replicates)

# Print the result
print('p-value =', p)
