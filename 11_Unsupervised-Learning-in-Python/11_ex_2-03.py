# Exercise 2-03: Hierarchical clustering of the grain data

import pandas as pd

samples = pd.read_csv('input/seeds-dendrosamples.csv', header=None).values
varieties = pd.read_csv('input/seeds-dendrovarieties.csv', header=None)[0].to_list()

# Perform the necessary imports
from scipy.cluster.hierarchy import linkage, dendrogram
import matplotlib.pyplot as plt

# Calculate the linkage: mergings
mergings = linkage(samples, method='complete')

# Plot the dendrogram, using varieties as labels
dendrogram(mergings, labels=varieties, leaf_rotation=90, leaf_font_size=6)
plt.show()
