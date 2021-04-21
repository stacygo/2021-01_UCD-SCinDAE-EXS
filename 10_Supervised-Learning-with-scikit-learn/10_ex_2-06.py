# Exercise 2-06: Fit & predict for regression

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

df = pd.read_csv('input/gm_2008_region.csv')

y = df['life'].values.reshape(-1, 1)
X_fertility = df['fertility'].values.reshape(-1, 1)

plt.scatter(X_fertility, y, color='blue')
plt.xlabel('Fertility')
plt.ylabel('Life Expectancy')

# Create the regressor: reg
reg = LinearRegression()

# Create the prediction space
prediction_space = np.linspace(min(X_fertility), max(X_fertility)).reshape(-1, 1)

# Fit the model to the data
reg.fit(X_fertility, y)

# Compute predictions over the prediction space: y_pred
y_pred = reg.predict(prediction_space)

# Print R^2
print(reg.score(X_fertility, y))

# Plot regression line
plt.plot(prediction_space, y_pred, color='black', linewidth=3)
plt.show()
