# Exercise 3-03: Specifying a model

import pandas as pd

df = pd.read_csv('input/hourly_wages.csv')

target = df['wage_per_hour'].values
predictors = df.drop(['wage_per_hour'], axis=1).values

# Import necessary modules
from tensorflow import keras
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Sequential

# Save the number of columns in predictors: n_cols
n_cols = predictors.shape[1]

# Set up the model: model
model = Sequential()

# Add the first layer
model.add(Dense(50, activation='relu', input_shape=(n_cols,)))

# Add the second layer
model.add(Dense(32, activation='relu'))

# Add the output layer
model.add(Dense(1))
