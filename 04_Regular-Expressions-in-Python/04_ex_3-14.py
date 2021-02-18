# Exercise 3-14: Understanding the difference

string = "I want to see that <strong>amazing show</strong> again!"

# Import re
import re

# Write a regex to eliminate tags
string_notags = re.sub(r"<.+?>", "", string)

# Print out the result
print(string_notags)