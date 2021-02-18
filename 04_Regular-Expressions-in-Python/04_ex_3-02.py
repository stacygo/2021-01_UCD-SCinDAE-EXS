# Exercise 3-02: Are they bots?

sentiment_analysis = "@robot9! @robot4& I have a good feeling that the show isgoing to be amazing! @robot9$ @robot7%"

# Import the re module
import re

# Write the regex
regex = r"@robot\d\W"

# Find all matches of regex
print(re.findall(regex, sentiment_analysis))

