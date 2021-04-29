# Exercise 3-05: Elbow method on distinct clusters

import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
from scipy.cluster.vq import whiten, kmeans

x = [17, 20, 35, 14, 37, 33, 14, 30, 35, 17, 11, 21, 13, 10, 81, 84, 87, 83, 90, 97, 94, 88, 89, 93, 92,
     82, 81, 92, 91, 22, 23, 25, 25, 27, 17, 17]
y = [4, 6, 0, 0, 4, 3, 1, 6, 5, 4, 6, 10, 8, 10, 97, 94, 99, 95, 95, 97, 99, 99, 94, 99, 90, 98, 100, 93,
     98, 15, 10, 0, 10, 7, 17, 15]

comic_con = pd.DataFrame({'x': x, 'y': y})

comic_con['x_scaled'] = whiten(comic_con['x'])
comic_con['y_scaled'] = whiten(comic_con['y'])

distortions = []
num_clusters = range(1, 7)

# Create a list of distortions from the kmeans function
for i in num_clusters:
    cluster_centers, distortion = kmeans(comic_con[['x_scaled', 'y_scaled']], i)
    distortions.append(distortion)

# Create a data frame with two lists - num_clusters, distortions
elbow_plot = pd.DataFrame({'num_clusters': num_clusters, 'distortions': distortions})

# Creat a line plot of num_clusters and distortions
sns.lineplot(x='num_clusters', y='distortions', data=elbow_plot)
plt.xticks(num_clusters)
plt.show()
