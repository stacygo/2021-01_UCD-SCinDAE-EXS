# Exercise 1-03: Artificial reviews

movie1 = "the most significant tension of _election_ is the potential relationship between a teacher and his student ."
movie2 = "the most significant tension of _rushmore_ is the potential relationship between a teacher and his student ."

# Select the first 32 characters of movie1
first_part = movie1[:32]

# Select from 43rd character to the end of movie1
last_part = movie1[42:]

# Select from 33rd to the 42nd character
middle_part = movie2[32:42]

# Print concatenation and movie2 variable
print(first_part + middle_part + last_part)
print(movie2)