# Exercise 2-05: Instantiate the model

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor

SEED = 1

df = pd.read_csv('input/auto.csv')

y = df['mpg']
X = pd.get_dummies(df.drop(['mpg'], axis=1))

# Split the data into 70% train and 30% test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=SEED)

# Instantiate a DecisionTreeRegressor dt
dt = DecisionTreeRegressor(max_depth=4, min_samples_leaf=0.26, random_state=SEED)
