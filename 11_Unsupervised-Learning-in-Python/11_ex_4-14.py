# Exercise 4-14: Recommend musical artists part II

import pandas as pd
from scipy.sparse import csr_matrix
from sklearn.decomposition import NMF
from sklearn.preprocessing import Normalizer, MaxAbsScaler
from sklearn.pipeline import make_pipeline

df = pd.read_csv('input/artists/scrobbler-small-sample.csv')
df_pivot = df.pivot(index='artist_offset', columns='user_offset', values='playcount').fillna(0)
artists = csr_matrix(df_pivot)
artist_names = pd.read_csv('input/artists/artists.csv', header=None)[0].to_list()

scaler = MaxAbsScaler()
nmf = NMF(n_components=20)
normalizer = Normalizer()

pipeline = make_pipeline(scaler, nmf, normalizer)
norm_features = pipeline.fit_transform(artists)

# Create a DataFrame: df
df = pd.DataFrame(norm_features, index=artist_names)

# Select row of 'Bruce Springsteen': artist
artist = df.loc['Bruce Springsteen']

# Compute cosine similarities: similarities
similarities = df.dot(artist)

# Display those with highest cosine similarity
print(similarities.nlargest())
