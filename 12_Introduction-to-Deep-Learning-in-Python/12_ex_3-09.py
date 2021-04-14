# Exercise 3-09: Last steps in classification models

import pandas as pd

df = pd.read_csv('input/titanic_all_numeric.csv')[:800]

predictors = df.drop(['survived'], axis=1).values

n_cols = predictors.shape[1]

# Import necessary modules
from tensorflow import keras
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Sequential
from tensorflow.keras.utils import to_categorical

# Convert the target to categorical: target
target = to_categorical(df.survived)
print(type(target))

# Set up the model
model = Sequential()

# Add the first layer
model.add(Dense(32, activation='relu', input_shape=(n_cols,)))

# Add the output layer
model.add(Dense(2, activation='softmax'))

# Compile the model
model.compile(optimizer='sgd', loss='categorical_crossentropy', metrics=['accuracy'])

# Fit the model
model.fit(predictors, target)
