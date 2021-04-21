# Exercise 1-07: k-Nearest Neighbors: Fit

import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.neighbors import KNeighborsClassifier

df = pd.read_csv('input/house-votes-84.csv')
df[df == '?'] = 'NaN'
df[df == 'y'] = 1
df[df == 'n'] = 0

imp = SimpleImputer(missing_values='NaN', strategy='most_frequent')
imp.fit(df.values)
df = pd.DataFrame(imp.transform(df.values), columns=df.columns)

# Create arrays for the features and the response variable
y = df['party'].values
X = df.drop('party', axis=1).values

# Create a k-NN classifier with 6 neighbors
knn = KNeighborsClassifier(n_neighbors=6)

# Fit the classifier to the data
knn.fit(X, y)
