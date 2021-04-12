# Exercise 2-09: Extracting the cluster labels

import pandas as pd
from scipy.cluster.hierarchy import linkage

samples = pd.read_csv('input/seeds-dendrosamples.csv', header=None).values
varieties = pd.read_csv('input/seeds-dendrovarieties.csv', header=None)[0].to_list()

mergings = linkage(samples, method='complete')

# Perform the necessary imports
from scipy.cluster.hierarchy import fcluster

# Use fcluster to extract labels: labels
labels = fcluster(mergings, 6, criterion='distance')

# Create a DataFrame with labels and varieties as columns: df
df = pd.DataFrame({'labels': labels, 'varieties': varieties})

# Create crosstab: ct
ct = pd.crosstab(df['labels'], df['varieties'])

# Display ct
print(ct)
