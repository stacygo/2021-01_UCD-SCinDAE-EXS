# Exercise 1-06: Extract a function

import pandas as pd

df = pd.DataFrame({'y1_gpa': [2.785877],
                   'y2_gpa': [2.052513],
                   'y3_gpa': [2.170544],
                   'y4_gpa': [0.065570],
                   'y1_z': [0.790863],
                   'y2_z': [0.028021],
                   'y3_z': [0.172322],
                   'y4_z': [-1.711179]})


def standardize(column):
    """Standardize the values in a column.

    Args:
        column (pandas Series): The data to standardize.

    Returns:
        pandas Series: the values as z-scores
    """
    # Finish the function so that it returns the z-scores
    z_score = (column - column.mean()) / column.std()
    return z_score


# Use the standardize() function to calculate the z-scores
df['y1_z'] = standardize(df['y1_gpa'])
df['y2_z'] = standardize(df['y2_gpa'])
df['y3_z'] = standardize(df['y3_gpa'])
df['y4_z'] = standardize(df['y4_gpa'])
