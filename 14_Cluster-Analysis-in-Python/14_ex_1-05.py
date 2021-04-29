# Exercise 1-05: Pokémon sightings: hierarchical clustering

from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd
from scipy.cluster.hierarchy import linkage, fcluster

x = [9, 6, 2, 3, 1, 7, 1, 6, 1, 7, 23, 26, 25, 23, 21, 23, 23, 20, 30, 23]
y = [8, 4, 10, 6, 0, 4, 10, 10, 6, 1, 29, 25, 30, 29, 29, 30, 25, 27, 26, 30]

df = pd.DataFrame({'x': x, 'y': y})

# Use the linkage() function to compute distance
Z = linkage(df.values, 'ward')

# Generate cluster labels
df['cluster_labels'] = fcluster(Z, 2, criterion='maxclust')

# Plot the points with seaborn
sns.scatterplot(x='x', y='y', hue='cluster_labels', data=df)
plt.show()
