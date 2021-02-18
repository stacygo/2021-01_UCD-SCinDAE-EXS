# Exercise 1-10: Finding a substring

import pandas as pd

movies_dict = {'200': "it's clear that he's passionate about his beliefs , and that he's not just a punk looking for an excuse to beat people up .",
               '201': "I believe you I always said that the actor actor actor is amazing in every movie he has played",
               '202': "it's astonishing how frightening the actor actor norton looks with a shaved head and a swastika on his chest."}

movies = pd.Series(data=movies_dict, index=['200', '201', '202'])

for movie in movies:
  	# Find if actor occurrs between 37 and 41 inclusive
    if movie.find("actor", 37, 42) == -1:
        print("Word not found")
    # Count occurrences and replace two by one
    elif movie.count("actor") == 2:
        print(movie.replace("actor actor", "actor"))
    else:
        # Replace three occurrences by one
        print(movie.replace("actor actor actor", "actor"))
