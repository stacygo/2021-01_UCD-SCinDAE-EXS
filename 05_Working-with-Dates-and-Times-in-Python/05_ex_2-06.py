# Exercise 2-06: Parsing pairs of strings as datetimes

from datetime import datetime

onebike_datetime_strings = [('2017-10-01 15:23:25', '2017-10-01 15:26:26'),
                            ('2017-10-01 15:42:57', '2017-10-01 17:49:59'),
                            ('2017-10-02 06:37:10', '2017-10-02 06:42:53'),
                            ('2017-10-02 08:56:45', '2017-10-02 09:18:03'),
                            ('2017-10-02 18:23:48', '2017-10-02 18:45:05')]

# Write down the format string
fmt = "%Y-%m-%d %H:%M:%S"

# Initialize a list for holding the pairs of datetime objects
onebike_datetimes = []

# Loop over all trips
for (start, end) in onebike_datetime_strings:
    trip = {'start': datetime.strptime(start, fmt), 'end': datetime.strptime(end, fmt)}

    # Append the trip
    onebike_datetimes.append(trip)
