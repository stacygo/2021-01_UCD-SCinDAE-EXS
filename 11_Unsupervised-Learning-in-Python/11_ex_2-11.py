# Exercise 2-11: t-SNE visualization of grain dataset

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('input/seeds.csv', header=None)
samples = df.iloc[:, :7].values

variety_names = {'1': 'Kama wheat', '2': 'Rosa wheat', '3': 'Canadian wheat'}
variety_numbers = df[7].to_list()

# Import TSNE
from sklearn.manifold import TSNE

# Create a TSNE instance: model
model = TSNE(learning_rate=200)

# Apply fit_transform to samples: tsne_features
tsne_features = model.fit_transform(samples)

# Select the 0th feature: xs
xs = tsne_features[:, 0]

# Select the 1st feature: ys
ys = tsne_features[:, 1]

# Scatter plot, coloring by variety_numbers
plt.scatter(xs, ys, c=variety_numbers)
plt.show()

