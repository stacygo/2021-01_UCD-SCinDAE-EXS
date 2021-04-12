# Exercise 4-10: PCA doesn't learn parts

import pandas as pd
from functions import show_as_image_modified

samples = pd.read_csv('input/lcd-digits.csv', header=None).values

# Import PCA
from sklearn.decomposition import PCA

# Create a PCA instance: model
model = PCA(n_components=7)

# Apply fit_transform to samples: features
features = model.fit_transform(samples)

# Call show_as_image on each component
for component in model.components_:
    show_as_image_modified(component)
