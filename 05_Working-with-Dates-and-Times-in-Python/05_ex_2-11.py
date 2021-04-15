# Exercise 2-11: Average trip time

import pandas as pd

df = pd.read_csv('input/capital-onebike.csv', parse_dates=['Start date', 'End date'])
df = df.rename(columns={"Start date": "start", "End date": "end"})

onebike_datetimes = df[['start', 'end']].to_dict('records')

# Initialize a list for all the trip durations
onebike_durations = []

for trip in onebike_datetimes:
    # Create a timedelta object corresponding to the length of the trip
    trip_duration = trip['end'] - trip['start']

    # Get the total elapsed seconds in trip_duration
    trip_length_seconds = trip_duration.total_seconds()

    # Append the results to our list
    onebike_durations.append(trip_length_seconds)

# What was the total duration of all trips?
total_elapsed_time = sum(onebike_durations)

# What was the total number of trips?
number_of_trips = len(onebike_durations)

# Divide the total duration by the number of trips
print(total_elapsed_time / number_of_trips)
