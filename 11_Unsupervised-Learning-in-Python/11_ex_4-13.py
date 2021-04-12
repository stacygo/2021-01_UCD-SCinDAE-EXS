# Exercise 4-13: Recommend musical artists part I

import pandas as pd
from scipy.sparse import csr_matrix

df = pd.read_csv('input/artists/scrobbler-small-sample.csv')
df_pivot = df.pivot(index='artist_offset', columns='user_offset', values='playcount').fillna(0)
artists = csr_matrix(df_pivot)

# Perform the necessary imports
from sklearn.decomposition import NMF
from sklearn.preprocessing import Normalizer, MaxAbsScaler
from sklearn.pipeline import make_pipeline

# Create a MaxAbsScaler: scaler
scaler = MaxAbsScaler()

# Create an NMF model: nmf
nmf = NMF(n_components=20)

# Create a Normalizer: normalizer
normalizer = Normalizer()

# Create a pipeline: pipeline
pipeline = make_pipeline(scaler, nmf, normalizer)

# Apply fit_transform to artists: norm_features
norm_features = pipeline.fit_transform(artists)
