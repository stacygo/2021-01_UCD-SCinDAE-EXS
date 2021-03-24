# Exercise 3-11: A one-sample bootstrap hypothesis test

import numpy as np
import functions

force_b = [0.172, 0.142, 0.037, 0.453, 0.355, 0.022, 0.502, 0.273, 0.72, 0.582, 0.198, 0.198,
           0.597, 0.516, 0.815, 0.402, 0.605, 0.711, 0.614, 0.468]

# Make an array of translated impact forces: translated_force_b
translated_force_b = force_b - np.mean(force_b) + 0.55

# Take bootstrap replicates of Frog B's translated impact forces: bs_replicates
bs_replicates = functions.draw_bs_reps(translated_force_b, np.mean, 10000)

# Compute fraction of replicates that are less than the observed Frog B force: p
p = np.sum(bs_replicates <= np.mean(force_b)) / 10000

# Print the p-value
print('p = ', p)



