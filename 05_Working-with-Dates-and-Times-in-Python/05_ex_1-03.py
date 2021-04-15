# Exercise 1-03: How many hurricanes come early?

import pickle

with open('input/florida_hurricane_dates.pkl', 'rb') as file:
    florida_hurricane_dates = pickle.load(file)

# Counter for how many before June 1
early_hurricanes = 0

# We loop over the dates
for hurricane in florida_hurricane_dates:
    # Check if the month is before June (month number 6)
    if hurricane.month < 6:
        early_hurricanes = early_hurricanes + 1

print(early_hurricanes)
