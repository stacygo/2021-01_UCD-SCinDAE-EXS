# Exercise 2-12: Regularization I: Lasso

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('input/gm_2008_region.csv')

y = df['life'].values
X = df.drop(['life', 'Region'], axis=1).values
df_columns = df.drop(['life', 'Region'], axis=1).columns

# Import Lasso
from sklearn.linear_model import Lasso

# Instantiate a lasso regressor: lasso
lasso = Lasso(alpha=0.4, normalize=True)

# Fit the regressor to the data
lasso.fit(X, y)

# Compute and print the coefficients
lasso_coef = lasso.fit(X, y).coef_
print(lasso_coef)

# Plot the coefficients
plt.plot(range(len(df_columns)), lasso_coef)
plt.xticks(range(len(df_columns)), df_columns.values, rotation=60)
plt.margins(0.02)
plt.show()
