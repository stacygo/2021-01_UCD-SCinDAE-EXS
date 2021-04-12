# Exercise 2-07: Different linkage, different hierarchical clustering!

import pandas as pd

df = pd.read_csv('input/eurovision-2016.csv')
df_pivot = df.pivot(index='From country', columns='To country', values='Televote Points')
samples = df_pivot.fillna(0).values
country_names = df_pivot.index.to_list()

# Perform the necessary imports
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, dendrogram

# Calculate the linkage: mergings
mergings = linkage(samples, method='single')

# Plot the dendrogram
dendrogram(mergings, labels=country_names, leaf_rotation=90, leaf_font_size=6)
plt.show()

