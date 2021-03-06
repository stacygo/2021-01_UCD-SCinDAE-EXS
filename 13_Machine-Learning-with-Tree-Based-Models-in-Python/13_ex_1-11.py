# Exercise 1-11: Evaluate the regression tree

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error as MSE

SEED = 3

df = pd.read_csv('input/auto.csv')

y = df['mpg']
X = pd.get_dummies(df.drop(['mpg'], axis=1))

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=SEED)

dt = DecisionTreeRegressor(max_depth=8, min_samples_leaf=0.13, random_state=SEED)
dt.fit(X_train, y_train)

# Compute y_pred
y_pred = dt.predict(X_test)

# Compute mse_dt
mse_dt = MSE(y_test, y_pred)

# Compute rmse_dt
rmse_dt = mse_dt**(1/2)

# Print rmse_dt
print("Test set RMSE of dt: {:.2f}".format(rmse_dt))
