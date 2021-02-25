# Exercise 1-10: Representing dates in different ways

# Import date
from datetime import date

# Create a date object
andrew = date(1992, 8, 26)

# Print the date in the format 'YYYY-MM'
print(andrew.strftime("%Y-%m"))

# Print the date in the format 'MONTH (YYYY)'
print(andrew.strftime("%B (%Y)"))

# Print the date in the format 'YYYY-DDD'
print(andrew.strftime("%Y-%j"))
