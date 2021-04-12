# Exercise 3-10: Dimension reduction of the fish measurements

import pandas as pd
from sklearn.preprocessing import StandardScaler

samples = pd.read_csv('input/fish.csv', header=None).iloc[:, 1:7].values
scaled_samples = StandardScaler().fit(samples).transform(samples)

# Import PCA
from sklearn.decomposition import PCA

# Create a PCA model with 2 components: pca
pca = PCA(n_components=2)

# Fit the PCA instance to the scaled samples
pca.fit(scaled_samples)

# Transform the scaled samples: pca_features
pca_features = pca.transform(scaled_samples)

# Print the shape of pca_features
print(pca_features.shape)
