# Exercise 3-11: Making predictions

import pandas as pd
from tensorflow import keras
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Sequential
from tensorflow.keras.utils import to_categorical

df = pd.read_csv('input/titanic_all_numeric.csv')[:800]
df_test = pd.read_csv('input/titanic_all_numeric.csv')[801:]

target = to_categorical(df.survived)
predictors = df.drop(['survived'], axis=1).values
pred_data = df_test.drop(['survived'], axis=1).values

n_cols = predictors.shape[1]

# Specify, compile, and fit the model
model = Sequential()
model.add(Dense(32, activation='relu', input_shape=(n_cols,)))
model.add(Dense(2, activation='softmax'))
model.compile(optimizer='sgd', loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(predictors, target)

# Calculate predictions: predictions
predictions = model.predict(pred_data)

# Calculate predicted probability of survival: predicted_prob_true
predicted_prob_true = predictions[:, 1]

# print predicted_prob_true
print(predicted_prob_true)
