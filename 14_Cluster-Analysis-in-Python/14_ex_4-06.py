# Exercise 4-06: TF-IDF of movie plots

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from functions import remove_noise

movies = pd.read_csv('input/movies_plot.csv')
plots = list(movies['Plot'])

# Initialize TfidfVectorizer
tfidf_vectorizer = TfidfVectorizer(max_df=0.75, min_df=0.1, max_features=50, tokenizer=remove_noise)

# Use the .fit_transform() method on the list plots
tfidf_matrix = tfidf_vectorizer.fit_transform(plots)
