# Exercise 2-15: Computing the Pearson correlation coefficient

import numpy as np


def pearson_r(x, y):
    """Compute Pearson correlation coefficient between two arrays."""
    # Compute correlation matrix: corr_mat
    corr_mat = np.corrcoef(x, y)

    # Return entry [0,1]
    return corr_mat[0,1]


versicolor_petal_length = [4.7, 4.5, 4.9, 4.,  4.6, 4.5, 4.7, 3.3, 4.6, 3.9, 3.5, 4.2, 4., 4.7,
                           3.6, 4.4, 4.5, 4.1, 4.5, 3.9, 4.8, 4., 4.9, 4.7, 4.3, 4.4, 4.8, 5.,
                           4.5, 3.5, 3.8, 3.7, 3.9, 5.1, 4.5, 4.5, 4.7, 4.4, 4.1, 4., 4.4, 4.6,
                           4., 3.3, 4.2, 4.2, 4.2, 4.3, 3., 4.1]

versicolor_petal_width = [1.4, 1.5, 1.5, 1.3, 1.5, 1.3, 1.6, 1., 1.3, 1.4, 1., 1.5, 1., 1.4, 1.3,
                          1.4, 1.5, 1., 1.5, 1.1, 1.8, 1.3, 1.5, 1.2, 1.3, 1.4, 1.4, 1.7, 1.5, 1.,
                          1.1, 1., 1.2, 1.6, 1.5, 1.6, 1.5, 1.3, 1.3, 1.3, 1.2, 1.4, 1.2, 1., 1.3,
                          1.2, 1.3, 1.3, 1.1, 1.3]

# Compute Pearson correlation coefficient for I. versicolor: r
r = pearson_r(versicolor_petal_length, versicolor_petal_width)

# Print the result
print(r)
