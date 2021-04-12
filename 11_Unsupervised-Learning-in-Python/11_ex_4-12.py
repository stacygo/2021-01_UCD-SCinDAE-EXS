# Exercise 4-12: Which articles are similar to 'Cristiano Ronaldo'?

import pandas as pd
from scipy.sparse import csr_matrix
from sklearn.decomposition import NMF

df = pd.read_csv('input/wikipedia/wikipedia-vectors.csv', index_col=0)
articles = csr_matrix(df.transpose())
titles = list(df.columns)

model = NMF(n_components=6)
model.fit(articles)
nmf_features = model.transform(articles)

# Perform the necessary imports
from sklearn.preprocessing import normalize

# Normalize the NMF features: norm_features
norm_features = normalize(nmf_features)

# Create a DataFrame: df
df = pd.DataFrame(norm_features, index=titles)

# Select the row corresponding to 'Cristiano Ronaldo': article
article = df.loc['Cristiano Ronaldo']

# Compute the dot products: similarities
similarities = df.dot(article)

# Display those with the largest cosine similarity
print(similarities.nlargest())
