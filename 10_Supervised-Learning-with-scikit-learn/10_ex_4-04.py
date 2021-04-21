# Exercise 4-04: Regression with categorical features

import pandas as pd
from sklearn.linear_model import Ridge
from sklearn.model_selection import cross_val_score

df = pd.read_csv('input/gm_2008_region.csv')
df = pd.get_dummies(df, drop_first=True)

y = df['life'].values
X = df.drop(['life'], axis=1).values

# Instantiate a ridge regressor: ridge
ridge = Ridge(alpha=0.5, normalize=True)

# Perform 5-fold cross-validation: ridge_cv
ridge_cv = cross_val_score(ridge, X, y, cv=5)

# Print the cross-validated scores
print(ridge_cv)
