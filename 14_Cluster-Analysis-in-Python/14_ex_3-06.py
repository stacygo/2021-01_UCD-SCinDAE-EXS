# Exercise 3-06: Elbow method on uniform data

import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
from scipy.cluster.vq import whiten, kmeans

x = [39, 42, 58, 43, 13, 32, 60, 13, 26, 27, 29, 51, 14, 50, 62, 59, 50, 62, 65, 17, 25, 45, 55, 48,
     42, 58, 68, 58, 37, 55]

y = [3, 7, 3, 3, 6, 5, 3, 4, 0, 9, 6, 3, 0, 7, 4, 1, 3, 0, 2, 5, 9, 5, 8, 6, 3, 1, 4, 2, 8, 7]

uniform_data = pd.DataFrame({'x': x, 'y': y})

uniform_data['x_scaled'] = whiten(uniform_data['x'])
uniform_data['y_scaled'] = whiten(uniform_data['y'])

distortions = []
num_clusters = range(2, 7)

# Create a list of distortions from the kmeans function
for i in num_clusters:
    cluster_centers, distortion = kmeans(uniform_data[['x_scaled', 'y_scaled']], i)
    distortions.append(distortion)

# Create a data frame with two lists - number of clusters and distortions
elbow_plot = pd.DataFrame({'num_clusters': num_clusters, 'distortions': distortions})

# Creat a line plot of num_clusters and distortions
sns.lineplot(x='num_clusters', y='distortions', data=elbow_plot)
plt.xticks(num_clusters)
plt.show()
