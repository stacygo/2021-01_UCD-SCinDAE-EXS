# Exercise 1-07: Time to join!

movie = "the film,however,is all good<\i>"

# Remove tags happening at the end and print results
movie_tag = movie.rstrip("<\i>")
print(movie_tag)

# Split the string using commas and print results
movie_no_comma = movie_tag.split(sep=",")
print(movie_no_comma)

# Join back together and print results
movie_join = ' '.join(movie_no_comma)
print(movie_join)