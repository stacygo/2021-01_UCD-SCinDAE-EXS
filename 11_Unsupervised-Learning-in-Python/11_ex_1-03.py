# Exercise 1-03: Clustering 2D points

import pandas as pd

points = pd.read_csv('input/points.csv').values
new_points = pd.read_csv('input/new_points.csv').values

# Import KMeans
from sklearn.cluster import KMeans

# Create a KMeans instance with 3 clusters: model
model = KMeans(n_clusters=3)

# Fit model to points
model.fit(points)

# Determine the cluster labels of new_points: labels
labels = model.predict(new_points)

# Print cluster labels of new_points
print(labels)
