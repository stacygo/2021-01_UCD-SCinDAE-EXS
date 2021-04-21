# Exercise 4-10: Centering and scaling your data

import numpy as np
import pandas as pd
from sklearn.preprocessing import scale

df = pd.read_csv('input/white-wine.csv')
df.loc[df['quality'] <= 5, 'quality'] = 1
df.loc[df['quality'] > 5, 'quality'] = 0

y = df['quality'].values
X = df.drop(['quality'], axis=1).values

# Scale the features: X_scaled
X_scaled = scale(X)

# Print the mean and standard deviation of the unscaled features
print("Mean of Unscaled Features: {}".format(np.mean(X)))
print("Standard Deviation of Unscaled Features: {}".format(np.std(X)))

# Print the mean and standard deviation of the scaled features
print("Mean of Scaled Features: {}".format(np.mean(X_scaled)))
print("Standard Deviation of Scaled Features: {}".format(np.std(X_scaled)))
