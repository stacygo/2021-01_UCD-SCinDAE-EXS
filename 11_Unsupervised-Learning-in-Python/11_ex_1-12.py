# Exercise 1-12: Which stocks move together?

import pandas as pd
from sklearn.pipeline import make_pipeline
from sklearn.cluster import KMeans
from sklearn.preprocessing import Normalizer

df = pd.read_csv('input/company-stock-movements-2010-2015-incl.csv')
movements = df.iloc[:, 1:].values
companies = df.iloc[:, 0].to_list()

normalizer = Normalizer()
kmeans = KMeans(n_clusters=10)
pipeline = make_pipeline(normalizer, kmeans)
pipeline.fit(movements)

# Predict the cluster labels: labels
labels = pipeline.predict(movements)

# Create a DataFrame aligning labels and companies: df
df = pd.DataFrame({'labels': labels, 'companies': companies})

# Display df sorted by cluster label
print(df.sort_values('labels'))
