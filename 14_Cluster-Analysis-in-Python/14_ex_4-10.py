# Exercise 4-10: Basic checks on clusters

import pandas as pd
from scipy.cluster.vq import whiten, kmeans, vq

fifa = pd.read_csv('input/fifa_18_sample_data.csv')

fifa['scaled_pac'] = whiten(fifa['pac'])
fifa['scaled_dri'] = whiten(fifa['dri'])
fifa['scaled_sho'] = whiten(fifa['sho'])

scaled_features = ['scaled_pac', 'scaled_dri', 'scaled_sho']

cluster_centers, _ = kmeans(fifa[scaled_features], 3)
fifa['cluster_labels'], _ = vq(fifa[scaled_features], cluster_centers)

# Print the size of the clusters
print(fifa.groupby('cluster_labels')['ID'].count())

# Print the mean value of wages in each cluster
print(fifa.groupby('cluster_labels')['eur_wage'].mean())
