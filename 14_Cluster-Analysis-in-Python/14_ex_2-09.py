# Exercise 2-09: Create a dendrogram

import pandas as pd
from matplotlib import pyplot as plt
from scipy.cluster.vq import whiten
from scipy.cluster.hierarchy import fcluster, linkage
from scipy.cluster.hierarchy import dendrogram

x = [17, 20, 35, 14, 37, 33, 14, 30, 35, 17, 11, 21, 13, 10, 81, 84, 87, 83, 90, 97, 94, 88, 89, 93, 92,
     82, 81, 92, 91, 22, 23, 25, 25, 27, 17, 17]
y = [4, 6, 0, 0, 4, 3, 1, 6, 5, 4, 6, 10, 8, 10, 97, 94, 99, 95, 95, 97, 99, 99, 94, 99, 90, 98, 100, 93,
     98, 15, 10, 0, 10, 7, 17, 15]

comic_con = pd.DataFrame({'x': x, 'y': y})

comic_con['x_scaled'] = whiten(comic_con['x'])
comic_con['y_scaled'] = whiten(comic_con['y'])

distance_matrix = linkage(comic_con[['x_scaled', 'y_scaled']], method='complete', metric='euclidean')
comic_con['cluster_labels'] = fcluster(distance_matrix, 2, criterion='maxclust')

# Create a dendrogram
dn = dendrogram(distance_matrix)

# Display the dendogram
plt.show()
