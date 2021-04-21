# Exercise 3-08: Train an RF regressor

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

SEED = 2

df = pd.read_csv('input/bikes.csv')

y = df['cnt']
X = df.drop(['cnt'], axis=1)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=SEED)

# Instantiate rf
rf = RandomForestRegressor(n_estimators=25, random_state=SEED)

# Fit rf to the training set
rf.fit(X_train, y_train)
