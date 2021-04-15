# Exercise 3-13: Cleaning daylight saving data with fold

import pandas as pd
from dateutil import tz

df = pd.read_csv('input/capital-onebike.csv', parse_dates=['Start date', 'End date'])
df = df.rename(columns={"Start date": "start", "End date": "end"})
df['start'] = df['start'].dt.tz_localize('America/New_York', ambiguous=True)
df['end'] = df['end'].dt.tz_localize('America/New_York', ambiguous=True)

onebike_datetimes = df[['start', 'end']].to_dict('records')

trip_durations = []
for trip in onebike_datetimes:
    # When the start is later than the end, set the fold to be 1
    if trip['start'] > trip['end']:
        trip['end'] = tz.enfold(trip['end'])
    # Convert to UTC
    start = trip['start'].astimezone(tz.UTC)
    end = trip['end'].astimezone(tz.UTC)

    # Subtract the difference
    trip_length_seconds = (end-start).total_seconds()
    trip_durations.append(trip_length_seconds)

# Take the shortest trip duration
print("Shortest trip: " + str(min(trip_durations)))
