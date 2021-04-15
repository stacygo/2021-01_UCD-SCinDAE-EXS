# Exercise 2-06: Parsing pairs of strings as datetimes

import pandas as pd
from datetime import datetime

df = pd.read_csv('input/capital-onebike.csv')
df = df.rename(columns={"Start date": "start", "End date": "end"})

onebike_datetime_strings = df[['start', 'end']].to_records(index=False)

# Write down the format string
fmt = "%Y-%m-%d %H:%M:%S"

# Initialize a list for holding the pairs of datetime objects
onebike_datetimes = []

# Loop over all trips
for (start, end) in onebike_datetime_strings:
    trip = {'start': datetime.strptime(start, fmt), 'end': datetime.strptime(end, fmt)}

    # Append the trip
    onebike_datetimes.append(trip)
