# Exercise 4-07: NMF learns topics of documents

import pandas as pd
from scipy.sparse import csr_matrix
from sklearn.decomposition import NMF

df = pd.read_csv('input/wikipedia/wikipedia-vectors.csv', index_col=0)
articles = csr_matrix(df.transpose())
titles = list(df.columns)
words = pd.read_csv('input/wikipedia/wikipedia-vocabulary-utf8.txt', header=None)[0].to_list()

model = NMF(n_components=6)
model.fit(articles)

# Create a DataFrame: components_df
components_df = pd.DataFrame(model.components_, columns=words)

# Print the shape of the DataFrame
print(components_df.shape)

# Select row 3: component
component = components_df.iloc[3]

# Print result of nlargest
print(component.nlargest())
