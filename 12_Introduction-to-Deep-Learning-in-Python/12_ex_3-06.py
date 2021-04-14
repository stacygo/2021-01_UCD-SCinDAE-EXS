# Exercise 3-06: Fitting the model

import pandas as pd

df = pd.read_csv('input/hourly_wages.csv')

target = df['wage_per_hour'].values
predictors = df.drop(['wage_per_hour'], axis=1).values

# Import necessary modules
from tensorflow import keras
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Sequential

# Specify the model
n_cols = predictors.shape[1]
model = Sequential()
model.add(Dense(50, activation='relu', input_shape = (n_cols,)))
model.add(Dense(32, activation='relu'))
model.add(Dense(1))

# Compile the model
model.compile(optimizer='adam', loss='mean_squared_error')

# Fit the model
model.fit(predictors, target)
