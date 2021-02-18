# Exercise 1-11: Where's the word?

import pandas as pd

movies_dict = {'137': "heck , jackie doesn't even have enough money for a haircut , looks like , much less a personal hairstylist .",
               '138': "in condor , chan plays the same character he's always played , himself , a mixture of bruce lee and tim allen , a master of both kung-fu and slapstick-fu ."}

movies = pd.Series(data=movies_dict, index=['137', '138'])

for movie in movies:
    # Find the first occurrence of word
    print(movie.find("money", 12, 51))

for movie in movies:
    try:
        # Find the first occurrence of word
        print(movie.index("money", 12, 51))
    except ValueError:
        print("substring not found")
