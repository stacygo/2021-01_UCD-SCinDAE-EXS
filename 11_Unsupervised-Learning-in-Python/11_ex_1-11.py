# Exercise 1-11: Clustering stocks using KMeans

import pandas as pd
from sklearn.pipeline import make_pipeline
from sklearn.cluster import KMeans

df = pd.read_csv('input/company-stock-movements-2010-2015-incl.csv')
movements = df.iloc[:, 1:].values

# Import Normalizer
from sklearn.preprocessing import Normalizer

# Create a normalizer: normalizer
normalizer = Normalizer()

# Create a KMeans model with 10 clusters: kmeans
kmeans = KMeans(n_clusters=10)

# Make a pipeline chaining normalizer and kmeans: pipeline
pipeline = make_pipeline(normalizer, kmeans)

# Fit pipeline to the daily price movements
pipeline.fit(movements)
