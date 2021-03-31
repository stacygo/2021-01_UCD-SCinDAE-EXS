# Exercise 1-08: k-Nearest Neighbors: Predict

import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer

df = pd.read_csv('input/house-votes-84.csv')
df[df == '?'] = 'NaN'
df[df == 'y'] = 1
df[df == 'n'] = 0

imp = SimpleImputer(missing_values='NaN', strategy='most_frequent')
imp.fit(df.values)
df = pd.DataFrame(imp.transform(df.values), columns=df.columns)

X_new_data = {'0': [0.696469], '1': [0.286139], '2': [0.226851], '3': [0.551315],
              '4': [0.719469], '5': [0.423106], '6': [0.980764], '7': [0.68483],
              '8': [0.480932], '9': [0.392118], '10': [0.343178], '11': [0.72905],
              '12': [0.438572], '13': [0.059678], '14': [0.398044], '15': [0.737995]}
X_new = pd.DataFrame.from_dict(X_new_data)

# Import KNeighborsClassifier from sklearn.neighbors
from sklearn.neighbors import KNeighborsClassifier

# Create arrays for the features and the response variable
y = df['party'].values
X = df.drop('party', axis=1).values

# Create a k-NN classifier with 6 neighbors: knn
knn = KNeighborsClassifier(n_neighbors=6)

# Fit the classifier to the data
knn.fit(X, y)

# Predict the labels for the training data X
y_pred = knn.predict(X)

# Predict and print the label for the new data point X_new
new_prediction = knn.predict(X_new)
print("Prediction: {}".format(new_prediction))
