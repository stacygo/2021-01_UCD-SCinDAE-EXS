# Exercise 2-12: A t-SNE map of the stock market

import pandas as pd
from sklearn.preprocessing import normalize
import matplotlib.pyplot as plt

df = pd.read_csv('input/company-stock-movements-2010-2015-incl.csv')
movements = df.iloc[:, 1:].values
companies = df.iloc[:, 0].to_list()

normalized_movements = normalize(movements)

# Import TSNE
from sklearn.manifold import TSNE

# Create a TSNE instance: model
model = TSNE(learning_rate=50)

# Apply fit_transform to normalized_movements: tsne_features
tsne_features = model.fit_transform(normalized_movements)

# Select the 0th feature: xs
xs = tsne_features[:, 0]

# Select the 1th feature: ys
ys = tsne_features[:, 1]

# Scatter plot
plt.scatter(xs, ys, alpha=0.5)

# Annotate the points
for x, y, company in zip(xs, ys, companies):
    plt.annotate(company, (x, y), fontsize=5, alpha=0.75)
plt.show()

