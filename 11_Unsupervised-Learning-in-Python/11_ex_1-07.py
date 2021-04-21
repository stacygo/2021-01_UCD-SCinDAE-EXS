# Exercise 1-07: Evaluating the grain clustering

import pandas as pd
from sklearn.cluster import KMeans

df = pd.read_csv('input/seeds.csv', header=None)
samples = df.iloc[:, :7].values

variety_names = {1: 'Kama wheat', 2: 'Rosa wheat', 3: 'Canadian wheat'}
varieties = df[7].map(variety_names).to_list()

# Create a KMeans model with 3 clusters: model
model = KMeans(n_clusters=3)

# Use fit_predict to fit model and obtain cluster labels: labels
labels = model.fit_predict(samples)

# Create a DataFrame with labels and varieties as columns: df
df = pd.DataFrame({'labels': labels, 'varieties': varieties})

# Create crosstab: ct
ct = pd.crosstab(df['labels'], df['varieties'])

# Display ct
print(ct)
