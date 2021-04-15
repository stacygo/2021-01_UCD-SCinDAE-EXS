# Exercise 1-09: Printing dates in a friendly format

import pickle

with open('input/florida_hurricane_dates.pkl', 'rb') as file:
    florida_hurricane_dates = pickle.load(file)

# Assign the earliest date to first_date
first_date = min(florida_hurricane_dates)

# Convert to ISO and US formats
iso = "Our earliest hurricane date: " + first_date.isoformat()
us = "Our earliest hurricane date: " + first_date.strftime("%m/%d/%Y")

print("ISO: " + iso)
print("US: " + us)
