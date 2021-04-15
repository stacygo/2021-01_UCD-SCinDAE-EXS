# Exercise 2-03: Counting events before and after noon

import pandas as pd

df = pd.read_csv('input/capital-onebike.csv', parse_dates=['Start date', 'End date'])
df = df.rename(columns={"Start date": "start", "End date": "end"})

onebike_datetimes = df[['start', 'end']].to_dict('records')

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
