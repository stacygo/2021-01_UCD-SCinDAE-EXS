# Exercise 2-09: 5-fold cross-validation

import numpy as np
import pandas as pd

df = pd.read_csv('input/gm_2008_region.csv')

y = df['life'].values.reshape(-1, 1)
X = df.drop(['life', 'Region'], axis=1).values

# Import the necessary modules
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score

# Create a linear regression object: reg
reg = LinearRegression()

# Compute 5-fold cross-validation scores: cv_scores
cv_scores = cross_val_score(reg, X, y, cv=5)

# Print the 5-fold cross-validation scores
print(cv_scores)

print("Average 5-Fold CV Score: {}".format(np.mean(cv_scores)))
