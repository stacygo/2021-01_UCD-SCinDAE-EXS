# Exercise 4-12: Surrounding words

import re

sentiment_analysis = "You need excellent python skills to be a data scientist. Must be! Excellent python"

# Positive lookahead
look_ahead = re.findall(r"\w+(?=\spython)", sentiment_analysis)

# Print out
print(look_ahead)

# Positive lookbehind
look_behind = re.findall(r"(?<=[pP]ython\s)\w+", sentiment_analysis)

# Print out
print(look_behind)
