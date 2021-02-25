# Exercise 1-07: Putting a list of dates in order

import datetime

dates_scrambled = [datetime.date(1988, 8, 4),
                   datetime.date(1990, 10, 12),
                   datetime.date(2003, 4, 20),
                   datetime.date(1971, 9, 1),
                   datetime.date(1988, 8, 23),
                   datetime.date(1994, 8, 15),
                   datetime.date(2002, 8, 4),
                   datetime.date(1988, 5, 30)]

# Print the first and last scrambled dates
print(dates_scrambled[0])
print(dates_scrambled[-1])

# Put the dates in order
dates_ordered = sorted(dates_scrambled)

# Print the first and last ordered dates
print(dates_ordered[0])
print(dates_ordered[-1])
