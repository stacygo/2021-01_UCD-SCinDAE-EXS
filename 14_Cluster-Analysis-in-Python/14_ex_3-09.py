# Exercise 3-09: Uniform clustering patterns

import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
from scipy.cluster.vq import whiten, kmeans, vq

mouse = pd.read_csv('input/mouse.csv')

mouse['x_scaled'] = whiten(mouse['x'])
mouse['y_scaled'] = whiten(mouse['y'])

# Generate cluster centers
cluster_centers, distortion = kmeans(mouse[['x_scaled', 'y_scaled']], 3)

# Assign cluster labels
mouse['cluster_labels'], distortion_list = vq(mouse[['x_scaled', 'y_scaled']], cluster_centers)

# Plot clusters
sns.scatterplot(x='x_scaled', y='y_scaled',
                hue='cluster_labels', data=mouse)
plt.show()
