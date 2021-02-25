# Exercise 2-03: Counting events before and after noon

import datetime

onebike_datetimes = [{'start': datetime.datetime(2017, 10, 1, 15, 23, 25),
                      'end': datetime.datetime(2017, 10, 1, 15, 26, 26)},
                     {'start': datetime.datetime(2017, 10, 1, 15, 42, 57),
                      'end': datetime.datetime(2017, 10, 1, 17, 49, 59)},
                     {'start': datetime.datetime(2017, 10, 2, 6, 37, 10),
                      'end': datetime.datetime(2017, 10, 2, 6, 42, 53)},
                     {'start': datetime.datetime(2017, 10, 2, 8, 56, 45),
                      'end': datetime.datetime(2017, 10, 2, 9, 18, 3)},
                     {'start': datetime.datetime(2017, 10, 2, 18, 23, 48),
                      'end': datetime.datetime(2017, 10, 2, 18, 45, 5)},
                     {'start': datetime.datetime(2017, 10, 2, 18, 48, 8),
                      'end': datetime.datetime(2017, 10, 2, 19, 10, 54)},
                     {'start': datetime.datetime(2017, 10, 2, 19, 18, 10),
                      'end': datetime.datetime(2017, 10, 2, 19, 31, 45)},
                     {'start': datetime.datetime(2017, 10, 2, 19, 37, 32),
                      'end': datetime.datetime(2017, 10, 2, 19, 46, 37)}]

# Create dictionary to hold results
trip_counts = {'AM': 0, 'PM': 0}

# Loop over all trips
for trip in onebike_datetimes:
    # Check to see if the trip starts before noon
    if trip['start'].hour < 12:
        # Increment the counter for before noon
        trip_counts['AM'] += 1
    else:
        # Increment the counter for after noon
        trip_counts['PM'] += 1

print(trip_counts)
