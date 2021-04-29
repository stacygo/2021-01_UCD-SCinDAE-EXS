# Exercise 1-06: Pokémon sightings: k-means clustering

from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd
from scipy.cluster.vq import kmeans, vq

x = [9.0, 6.0, 2.0, 3.0, 1.0, 7.0, 1.0, 6.0, 1.0, 7.0, 23.0, 26.0, 25.0, 23.0, 21.0, 23.0, 23.0,
     20.0, 30.0, 23.0]
y = [8.0, 4.0, 10.0, 6.0, 0.0, 4.0, 10.0, 10.0, 6.0, 1.0, 29.0, 25.0, 30.0, 29.0, 29.0, 30.0, 25.0,
     27.0, 26.0, 30.0]

df = pd.DataFrame({'x': x, 'y': y})

# Compute cluster centers
centroids, _ = kmeans(df.values, 2)

# Assign cluster labels
df['cluster_labels'], _ = vq(df.values, centroids)

# Plot the points with seaborn
sns.scatterplot(x='x', y='y', hue='cluster_labels', data=df)
plt.show()
