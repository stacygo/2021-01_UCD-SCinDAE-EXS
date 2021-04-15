# Exercise 1-07: Putting a list of dates in order

import pickle

with open('input/florida_hurricane_dates.pkl', 'rb') as file:
    dates_scrambled = pickle.load(file)

# Print the first and last scrambled dates
print(dates_scrambled[0])
print(dates_scrambled[-1])

# Put the dates in order
dates_ordered = sorted(dates_scrambled)

# Print the first and last ordered dates
print(dates_ordered[0])
print(dates_ordered[-1])
