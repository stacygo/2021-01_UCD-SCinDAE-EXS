# Exercise 1-09: Printing dates in a friendly format

import datetime

florida_hurricane_dates = [datetime.date(1950, 8, 31),
                           datetime.date(1950, 9, 5),
                           datetime.date(1950, 10, 18),
                           datetime.date(1950, 10, 21),
                           datetime.date(1951, 5, 18),
                           datetime.date(1951, 10, 2),
                           datetime.date(1952, 2, 3)]

# Assign the earliest date to first_date
first_date = min(florida_hurricane_dates)

# Convert to ISO and US formats
iso = "Our earliest hurricane date: " + first_date.isoformat()
us = "Our earliest hurricane date: " + first_date.strftime("%m/%d/%Y")

print("ISO: " + iso)
print("US: " + us)
