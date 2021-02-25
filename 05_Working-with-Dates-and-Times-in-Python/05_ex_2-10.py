# Exercise 2-10: Turning pairs of datetimes into durations

import datetime

onebike_datetimes = [{'start': datetime.datetime(2017, 10, 1, 15, 23, 25),
                      'end': datetime.datetime(2017, 10, 1, 15, 26, 26)},
                     {'start': datetime.datetime(2017, 10, 1, 15, 42, 57),
                      'end': datetime.datetime(2017, 10, 1, 17, 49, 59)},
                     {'start': datetime.datetime(2017, 10, 2, 6, 37, 10),
                      'end': datetime.datetime(2017, 10, 2, 6, 42, 53)}]

# Initialize a list for all the trip durations
onebike_durations = []

for trip in onebike_datetimes:
    # Create a timedelta object corresponding to the length of the trip
    trip_duration = trip['end'] - trip['start']

    # Get the total elapsed seconds in trip_duration
    trip_length_seconds = trip_duration.total_seconds()

    # Append the results to our list
    onebike_durations.append(trip_length_seconds)
