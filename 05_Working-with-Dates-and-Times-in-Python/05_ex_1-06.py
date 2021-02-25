# Exercise 1-06: Counting events per calendar month

import datetime

florida_hurricane_dates = [datetime.date(1950, 8, 31),
                           datetime.date(1950, 9, 5),
                           datetime.date(1950, 10, 18),
                           datetime.date(1950, 10, 21),
                           datetime.date(1951, 5, 18)]

# A dictionary to count hurricanes per calendar month
hurricanes_each_month = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0,
                         7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0}

# Loop over all hurricanes
for hurricane in florida_hurricane_dates:
    # Pull out the month
    month = hurricane.month
    # Increment the count in your dictionary by one
    hurricanes_each_month[month] += 1

print(hurricanes_each_month)
