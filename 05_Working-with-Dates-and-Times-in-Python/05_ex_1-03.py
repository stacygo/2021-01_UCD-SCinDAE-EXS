# Exercise 1-03: How many hurricanes come early?

import datetime

florida_hurricane_dates = [datetime.date(1950, 8, 31),
                           datetime.date(1950, 9, 5),
                           datetime.date(1950, 10, 18)]

# Counter for how many before June 1
early_hurricanes = 0

# We loop over the dates
for hurricane in florida_hurricane_dates:
    # Check if the month is before June (month number 6)
    if hurricane.month < 6:
        early_hurricanes = early_hurricanes + 1

print(early_hurricanes)
