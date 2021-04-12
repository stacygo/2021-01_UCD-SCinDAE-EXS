# Exercise 4-04: NMF features of the Wikipedia articles

import pandas as pd
from scipy.sparse import csr_matrix
from sklearn.decomposition import NMF

df = pd.read_csv('input/wikipedia/wikipedia-vectors.csv', index_col=0)
articles = csr_matrix(df.transpose())
titles = list(df.columns)

model = NMF(n_components=6)
model.fit(articles)
nmf_features = model.transform(articles)

# Create a pandas DataFrame: df
df = pd.DataFrame(nmf_features, index=titles)

# Print the row for 'Anne Hathaway'
print(df.loc['Anne Hathaway'])

# Print the row for 'Denzel Washington'
print(df.loc['Denzel Washington'])
